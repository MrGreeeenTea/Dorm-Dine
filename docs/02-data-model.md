---
title: Data Model
parent: Technical Docs
nav_order: 1
---

{: .no_toc }
# Data Model

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

# ERD
Compared to the original design, six tables were removed that were modeled but never actually connected to the application (no model, route, or template ever accessed them):

`language`, `user_language` - User multilingualism was planned but never used anywhere in the code.

`icon` - Icon assignment for dishes now runs entirely through automatic keyword detection in the backend (text search in name/description/ingredients), instead of a  table.

`kitchen_proof` - The planned kitchen cleanliness verification (photo + timestamp) was never implemented.

`dish_photo` - Multiple photos per dish were planned but never implemented.

`notification` - The notification system existed only as a table, with no logic behind it.

The tables that are actually used in the code were kept: `dorm`, `user, dish`, `dish_order`, `message`, `tag`, `dish_tag`.

## Before:

![data model - Dorm & Dine](assets\images\Dorm&Dine_Data_Model.drawio.png)

## After:

![data model - Dorm & Dine](assets\images\Dorm&Dine_Data_Model(final).png)
