# CreepRescue

## What it does

If you're out with someone you don't know or are in an unfamiliar area, with this web app, you can share your current location with your friends and family. If you ever find yourself stuck in an awkward situation and are unable to leave, you can use this app to receive a fake call and make your sneaky escape. To all those people, you don't want to give your personal phone number to, you can give the number of the chatbot which replies to texts with sassy remarks and you can be at peace.


## How it's built

This app is built using Python and Flask for the backend and HTML, CSS for the frontend. It uses the Google Maps Geolocation API and the Google Maps URLs to construct a sharable URL that shows the accurate position of the user. Twilio is used to make send a call to the user when they request to receive a fake call. The chatbot also uses Twilio to carry out 2 way messaging. The app uses an sqlite3 database to maintain the details of the user.


## Login/Signup

![cr1](https://user-images.githubusercontent.com/67470527/150697446-1c208bf8-bbc9-456f-8cb4-7a4b17a9438a.PNG)

## Home

![cr2](https://user-images.githubusercontent.com/67470527/150697456-7c2f73c8-480e-4272-ba13-8e8a5b33f020.PNG)

## Share current Location

![cr3](https://user-images.githubusercontent.com/67470527/150697482-a817d0d9-5927-4447-82f7-93d6dab7e47f.PNG)

## Receive a Fake Call

![cr4](https://user-images.githubusercontent.com/67470527/150697485-4e293e40-11bf-4799-a826-bcb6a49399ae.PNG)

## Get Chatbot Number

![cr5](https://user-images.githubusercontent.com/67470527/150697505-3209c6b6-1134-4a0c-8e5e-6a6fa4049782.PNG)