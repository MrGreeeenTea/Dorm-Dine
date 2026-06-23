---
title: Lars Unger
parent: Individual Contributions
nav_order: 3
---

{: .no_toc }
# Lars Unger

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,3

### Personal goals

During the collaboration on this project, I would like to further develop myself in the context of practical teamwork and project-based learning. By working with tools such as GitHub and other modern development technologies, I hope to gain valuable experience that will prepare me for my future professional career and help me connect academic learning with my real world working environment.

In addition, I am highly interested in expanding my technical knowledge, especially in areas such as Python and Website Building. I see this project as a great opportunity to strengthen both my programming skills and my ability to work effectively within a development team.

---

## Eidesstattliche Erklärung

[Lars Unger, Matrikelnr.: 77206621704]

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Order process UI | I created the user interface for the ordering process, including the order overview and payment choice. I am proud of this because the process became clear, fast and easy to understand for the user. It also made the app feel more complete, because users could not only view meals but actually go through the steps of ordering one | The biggest challenge was understanding how the UI connects to the database logic. I had to learn how information changes during an order, for example when a meal is selected or when the number of available portions is updated. This was difficult at first, but it helped me understand how frontend and backend work together |
| 2 | Meal overview UI | I built the meal overview page where users can browse available dishes. I am proud of this because it is one of the most important screens for the buyer side of our app. The page had to be simple, readable and visually clear, so users can quickly compare meals, prices, cooks, dorms and pickup times | This was one of the first screens I worked on, so I had to learn how to display database information inside the HTML template. At the beginning I worked with static example meals, but later I changed it so the page uses real data from the database. Understanding this transition from static content to dynamic content was a big step for me |
| 3 | Landing Page UI | I created the landing page as the first screen users see when opening the app. I am proud of it because I kept it simple and focused on the core idea of Dorm & Dine: reducing food waste and offering affordable homemade meals for students living in dorms. The clean design helps users immediately understand what the app is about | The challenge was not to overload the page with too much information. I had to focus on the most important message and make the design look clean while still fitting the overall style of the application. This helped me think more about user experience and not only about writing code that works |



## Design Decisions that I led

1. [DD #02](../design-decisions/dd-02.md)
2. [DD #07](../design-decisions/dd-07.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used | Extra Info |
| :-- | :-- | :-- | :-- |
| Meal overview UI / feed page| Current feed.html layout showing available meals with dish name, description, cook, dorm, price, pickup time, available portions and order button | See left | This was one of my first UI tasks. I started with static meal cards and later changed the page so it displays real dish data from the database.
| Database-connected UI changes | Current order_view.html and related order flow in app.py | See left | This includes the order page, payment choice between cash and PayPal, confirmation messages and navigation back to the meal overview.
| UI debugging and improvements | Several smaller commits fixing layout, buttons, formatting, pickup time display and template errors | See left | A big part of my contribution was not only creating pages, but repeatedly fixing small UI and template problems until the screens worked properly.
|  |  |  |  |
|  |  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |     Chat GPT    |        Design for D&D Logo        |               static-images   & Landing Page               |              Bitte erstelle ein Logo für eine Website für Studenten Namens Dorm & Dine               |
| 02  |    Chat GPT     |        Design for Food Icons        |              static-images  &   templates-orderview,feed                 |               Bitte erstelle für die genannte Website Icons für 10 Gerichte: Beispiel Pasta, Burger etc.              |
| ... |         |                |                                 |                             |
