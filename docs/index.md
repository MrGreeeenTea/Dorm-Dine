---
title: Home
nav_order: 0
---


# Dorm & Dine

Dorm & Dine is a student-to-student food platform built for dormitory life. Instead of ordering expensive delivery or cooking alone for one, students can buy and sell home-cooked meals within their own building. Cooks cover their ingredient costs by selling extra portions, buyers get fresh food, and both sides skip the waste, the packaging, and the delivery fee.

## Sample App Screen

# Landing page

![landing page](assets\images\landing_page.png)
---

## Improvements / Refinements since First Submission

[Assess implementation of improvements / refinements since First Submission (as presented during Oral Examination).]

**Julia:**

* Cook can see user information of people who made a reservation on their uploaded dishes on dishboard and can't order his own meals anymore

* Adjustions to Login, Register and Edit Profile Form 

* Edit Profile Form shows current data while editing and now you can choose to become a cook in the Edit Profile Section


**Luisa:**

* Backend Time Validator added to enforce the cook cannot set an endtime that is before the starttime. (forms.py + post_meal.html)

* Edit and delete meals was added as a fuctionality to my dishes on dashboard. Deletion can only be done if no one has ordered the dish! (app.py + dashboard.html)

* Db sample was missing user3 in commit, small fix (db.py)

* Made it so only cooks can post meals. Previously a user who isn't a cook could /post. (app.py)

**Angelina Ye:**

* **UI Screens updated** - added new pictures
* **Database updated** - removed unused tables,  cleaned up the remaining models
* **Data model changed** - updated the ERD to match the tables actually in use, added a before/after comparison
* **Value proposition updated** - added a before/after comparison to the scope description: which features were actually implemented and which were dropped
* **Testing & small bugfixes** - translated leftover German UI text into English 

**Lars Unger:**

* Added PNG icons for 10 common food categories plus a fallback "others" icon (static/images)

* Integrated icon display into the dish feed and meal detail views (templates/feed.html; templates/meal_detail.html)

* Implemented keyword-based matching logic that selects the icon whose food category best matches each dish (app.py)
* 
{: .fs-2 }
Last build: {{ site.time | date: '%d %b %Y, %R%:z' }}
