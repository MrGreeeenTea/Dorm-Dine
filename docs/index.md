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

# Feed

![Feed](assets\images\feed.png)
---

# Dashbaord

![Dashboard](assets\images\dashboard.png)
---

# Profil

![Profil](assets\images\profil.png)
---

## Improvements / Refinements since First Submission

[Assess implementation of improvements / refinements since First Submission (as presented during Oral Examination).]

Julia:

-Cook can see user information of people who made a reservation on their uploaded dishes on dishboard

-Adjustions to Login, Register and Edit Profile Form 

-Edit Profile Form shows current data while editing and now you can choose to become a cook in the Edit Profile Section


Luisa:

-Backend Time Validator added to enforce the cook cannot set an endtime that is before the starttime. (forms.py + post_meal.html)

-Edit and delete meals was added as a fuctionality to my dishes on dashboard. Deletion can only be done if no one has ordered the dish! (app.py + dashboard.html)

-Db sample was missing user3 in commit, small fix (db.py)

-Made it so only cooks can post meals. Previously a user who isn't a cook could /post. (app.py)


{: .fs-2 }
Last build: {{ site.time | date: '%d %b %Y, %R%:z' }}
