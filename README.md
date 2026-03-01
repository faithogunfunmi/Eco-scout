# Eco-scout
Hack For Humanity 2026
---

## Inspiration
Many popular clothing stores aren't sustainable or ethical, and many people simply don't have the time or energy to go out of their way to research better alternatives while shopping. We wanted to bridge the gap between convenience and conscious consumerism by bringing the ethical alternatives directly to the user, the exact moment they need them.

## What it does
EcoScout is a Chrome extension that acts as an ethical and sustainable shopping assistant. When you visit an online clothing website, EcoScout reads the active URL and instantly cross-references the brand with our custom database.

When you open the extension, you are greeted with a UI that displays an overall rating on a dynamic visual meter, alongside specific Ethics and Sustainability metrics. If you are shopping on a fast-fashion site (like Shein or Zara), EcoScout throws a warning flag and immediately provides a curated list of sustainable, ethical alternative brands (like Patagonia or Pact) that match the clothing category you are currently browsing.

## How we built it
We developed the user interface using React, JavaScript, and HTML/CSS.

We conducted our own research to identify popular fast fashion companies as well as sustainable and ethical alternatives. Based on our findings, we made our own database by using Firebase to store fast fashion companies and our recommended companies. We created a Python program to match the detected URL to fast fashion brand names in our database. It also identifies the recommendation names and links. 

## Challenges we ran into
Some challenges we ran into were keeping ourselves on the same page with our GitHub pushes. Luckily for us, we did not run into any major merge conflicts or code loss but making sure that everyone was working on the same/similar code could get convoluted at times because a lot of us were new to collaborative coding. Despite this challenge, we constantly kept in touch and updated each other on our status, so we were able to get everyone on the same page by the end.

## Accomplishments that we're proud of
Some accomplishments we are proud of are creating a custom database of over 70 companies, distinguishing fast-fashion companies and their alternatives. Another accomplishment was getting the backend to receive a fast-fashion company, searching for its alternatives, and giving the frontend the recommended company name and URL.

## What we learned
For the front-end, we learned how to create a Google Extension, 
For the back-end, we learned how to use the database Firestorm and access it with our Python program.

## What's next for EcoScout?
Some future advancements we have planned are to create a bigger database to include a wider range of fast-fashion companies and alternatives. We would also like to add more criteria to our evaluation system of sustainable, ethical, and mixed ratings. Additionally, we plan to enhance our Google Extension by adding tabs to provide more information to the user about the recommended companies. Moreover, we would like to implement a notification system that alerts the user whenever they open an online store that's also located in our database.

