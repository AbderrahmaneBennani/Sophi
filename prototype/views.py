# from http.client import HTTPResponse
from django.shortcuts import render
import os
import openai
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
openai.api_key = os.environ.get('OPENAI_API_KEY')
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # print("wlkjdflkasjdlkfjaslkdfjlaksjfdaslkjdf")
    # return HttpResponse("hello")
    return render(request, 'prototype/index.html', {})

# @csrf_exempt
def chat(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Employee:\nI think there is better software to manage our todos\nHR:\nYour anonymous feedback has been noted. Thank you!\n===\nEmployee:\nI think a co-worker is trying to flirt with me\nHR:\nThere are a few things you can do if you feel you are being harassed at work. First, you can try to talk to the person who is harassing you and ask them to stop. If that does not work, you can speak to your supervisor or HR department and let them know what is happening. They may be able to help resolve the situation. Finally, if you feel like you are in danger, \n===\nEmployee: a co-worker is being flirtatious towards me\nHR:If you are being harassed or think you may be, but are too scared to go forward, educating yourself on the facts is a great way to gain confidence to stand up for yourself\n===\nEmployee:" + msg +"\nHR:\n",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["==="]
        )

        print(response)

        return HttpResponse(response['choices'][0]['text'])

    return HttpResponse("error")

