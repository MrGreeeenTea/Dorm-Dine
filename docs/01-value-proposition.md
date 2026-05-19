---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## The Problem

Cooking in student dormitories is time-consuming, expensive, and often leads to unnecessary food waste. Since students typically cook small portions just for themselves, they end up paying more for smaller package sizes at the supermarket. A poor trade-off that rarely feels worth the effort. As a result, many students fall back on unhealthy convenience foods or expensive delivery services like UberEats and Wolt, spending money they don't have on meals that don't satisfy.

## Our Solution

Dorm & Dine is a web-based platform that connects students within the same dormitory. Students who enjoy cooking can offer and sell extra portions of their home-cooked meals. Students who don't want to cook can browse nearby listings and pick up fresh, affordable food, that is made by fellow students, right where they live.
The app allows users to register, create weekly meal plans, list dishes for sale, and browse available offers. It is designed to be simple and accessible: find a meal, place an order, pick it up from down the hall.
Dorm & Dine does not promise restaurant-quality logistics or a full marketplace infrastructure. It is a lightweight community tool built specifically for dormitory life: reducing waste, enabling a small side income for cooks, and making it easier for everyone to eat well on a student budget.

## Target User(s)

Dorm & Dine is built for two kinds of students who already live under the same roof. They have different problems, but the same solution fixes both.

**Persona A — The Buyer** 

Julia Meier, 21 years old, 3rd semester, Business Administration

Julia moved into her dorm half a year ago and still hasn't figured out the whole cooking thing. It's not that she can't cook, but she just doesn't see the point when it's only for herself. She buys a bag of spinach, uses a handful, and watches the rest go soggy in the fridge. She's tried meal prepping once. It lasted four days before she gave up and ordered pizza.
Most evenings she ends up scrolling through Wolt or UberEats, feeling vaguely guilty about spending 14€ on a burger that arrives lukewarm in a pile of plastic. She knows it's not sustainabl, but cooking a full meal at 9pm after a long day just feels like too much. So she doesn't.

What Julia actually wants is simple: something warm, real, and cheap, without having to think too hard about it. She doesn't need a gourmet experience. 

Dorm & Dine is exactly that for her. She opens the app, sees what's available two floors up, taps reserve, and shows up at the right time. No account needed just to browse. No delivery fee. No guilt.


**Persona B — The Cook**

Lars Müller, 23 years old, 5th semester, Computer Science

Lars actually likes cooking. He makes proper food like curries, stir-fries, the occasional homemade soup and he always makes too much, because cooking for one portion feels almost pointless.
The extra food usually ends up in a container in his fridge, eaten reluctantly over the next two days, or quietly thrown away when it's been there too long. He's not struggling financially, but as a student he notices every euro. The idea that his grocery bill could partly pay for itself is genuinely appealing.

He's also the kind of person who finds dorm life a bit more isolated than he expected. Cooking for neighbors gives him a small but real reason to interact with people he'd otherwise just nod at in the hallway.
With Dorm & Dine, Lars posts what he's cooking that evening, sets a price that covers his ingredients, and gets a knock on the door at pickup time. His food doesn't go to waste, his costs go down, and he slowly becomes the person on his floor that everyone knows makes great food.



##  Happy Path

![Happy Path - Buyer and Cook](assets\images\Happy_Path_DD.png)


---

## Target Scope

![UI screens scribbles](assets\images\UI_Screens_Scribbles.jpeg)

The scope of Dorm & Dine was defined at the start of the project by mapping out which screens and features are essential for the core user journey.

The app is structured around three groups of screens. Shared screens are accessible to everyone. 
The landing page can be browsed without an account, registration and login only appear when a user tries to place an order, and the profile page is available to both buyers and cooks. 

Buyer-specific screens cover the full journey from browsing the feed and viewing meal details, to confirming a reservation, tracking active orders, and submitting a rating after pickup. 

Cook-specific screens allow users to post a dish with price, portions, and pickup time, plan their meals for the week, manage their active offers, and respond to incoming order notifications.

## Ablaufdiagramm

![Ablaufdiagramm](assets\images\ablaufdiagramm1.png)

To clearly define the project's scope and ensure a shared understanding of how Dorm & Dine will function, we mapped out a tentative but comprehensive user flow diagram (Ablaufdiagramm).

The diagram serves as our structural foundation, guiding both our user interface design and our backend development priorities. It was purposefully created to visually map the users journey and help us identify which screens, user inputs, and background system actions are mandatory for a serviceable user experience. Using this flow we are able to pinpoint open design decisions and look for appropriate solutions. 
