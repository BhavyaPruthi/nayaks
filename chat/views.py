from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from chat.models import *
from chat.forms import UserForm, UserProfileForm
import json

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(
            request,
            'chat/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
            )
def stats(request):
    argument_list = Argument.objects.order_by('-upvote')
    theargument=argument_list[:1]
    person_list= Person.objects.all().order_by('person_name')
    maximum=0
    people={}
    for person in person_list:
        people[person.person_name]=0
    for argument in argument_list:
        people[argument.person.person_name]=people[argument.person.person_name]+argument.upvote
    for person in person_list:
        if(maximum<people[person.person_name]):
            maximum=people[person.person_name]
            maximump=person.person_name
    print(maximum)
    print(maximump)
    return render_to_response("chat/stats.html", locals(), context_instance=RequestContext(request))


def index(request):

    argument_list = Argument.objects.order_by('time')
    person_list = Person.objects.all().order_by('person_name')
    
    # party = Party.objects.get(party_name='AAP')
    # count_persons = Person.objects.filter(person_party=party)
    #print(count_persons)
    #print(len(count_persons))
        
    return render_to_response("chat/index.html", locals(), context_instance=RequestContext(request))
    
def vote(request):
    print("Function was called")
    results = {'success':False}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'vote'):
            pk = int(GET[u'pk'])
            vote = GET[u'vote']
            poll = Chat.argument.get(pk=pk)
            if vote == u"up":
                poll.up()
            elif vote == u"down":
                poll.down()
            results = {'success':True}
    json = simplejson.dumps(results)
    return render_to_response("chat/index.html", locals(), context_instance=RequestContext(request))



def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    print("Request Credentials")
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        print("Recieved Credentials")

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                print("Login Sucessful", username)
                return HttpResponseRedirect('/chat/session/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Nayak account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('chat/home.html', {}, context)




def test(request):
    print("data Recieved")
    if request.method == 'GET':
        response_data = {}

        if request.GET.get('vote'):
            post_text = request.GET.get('vote')     
            if(post_text=='upvote'):
                print("Upvote Recieved")
                response_data['val'] = int(request.GET.get('count'))+1
                print(response_data['val'])
                entry = Argument.objects.get(pk=int(request.GET.get('idd')))
                print(entry.upvote)
                entry.upvote=entry.upvote+1
                entry.save()

            elif(post_text=='downvote'):
                print("Downvote Recieved")
                response_data['val'] = int(request.GET.get('count'))+1
                entry = Argument.objects.get(pk=int(request.GET.get('idd')))
                entry.downvote=entry.downvote+1
                entry.save()
                


            # else:
            #     if int(request.GET.get('count')) == 0:
            #         response_data['val'] = 0
            #         return HttpResponse(
            #             json.dumps(response_data),
            #             content_type="application/json"
            #         )
            #     response_data['val'] = int(request.GET.get('count'))-1 

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

        if request.GET.get('the_post'):
            response_data['result'] = 'Result was successful.'
            response_data['name'] = 'Gourav Mittal'

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

    return HttpResponseRedirect('/')

