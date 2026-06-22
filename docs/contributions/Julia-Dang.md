---
title: Julia Dang
parent: Individual Contributions
nav_order: 2
---

# Julia Dang

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

1,7

### Personal goals

Zu Beginn des Kurses war ich sehr überwältigt von den Anforderungen, welche ich eigentlich sehr interessant finde, aber meiner Meinung nach sehr anspruchsvoll sind für mich. Deswegen möchte ich durch diesen Kurs und das Projekt die Grundlagen von Python sicher beherrschen und auch Spaß am Programmieren finden, da ich durch Schwierigkeiten schnell demotiviert bin.

---

## Eidesstattliche Erklärung

**[Julia Dang, Matrikelnr.: 77201600054]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Register | I learned various aspects of working in Full Stack Web Development. I built the form using Flask-WTF using validators, integrated it in the corresponding route. I learned about password hashing and integrated the database logic to create new users | I learned how to work step for step, at the beginning becoming familiar with Flask-WTF and the routing. Once it worked I started to implement the password hashing and database connection, that upon successful registration new user object instances would be added to the database. Even though everything didn't work out at first. After trying I was able to code a fully functional Register page |
| 2 | Login | I built the login form with Flask-WTF, implemented a authentication logic using Flask-Login Manager|  |
| 3 | Profile Editing | I built the update profile form with Flask-WTF. I made sure with @login_required and current_user that only the currently authenticated user can edit their own profile | I identified a problem in my edit profile form: If one field in the form would be left empty by the user because no changes in that attribute should be made, an empty input would had overwritten the existing data in the database. I fixed this by working with if-clauses |

## Design Decisions that I led

1. [DD #00](../design-decisions/dd-00.md)
2. [DD #08](../design-decisions/dd-07.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Create Forms with Validators on their corresponding route | [Commit 1](https://github.com/MrGreeeenTea/Dorm-Dine/commit/a77ad04fbcb672c9878eb1e54a6019f3199c2b27) | [Flask Mega Tutorial:Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms), [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/quickstart/#validating-forms) and [FSWD: Flask Routing](https://hwrberlin.github.io/fswd/flask.html) |
| Added Password Hashing, Login Manager, Connected the Forms to the Database | [Commit 2](https://github.com/MrGreeeenTea/Dorm-Dine/commit/47569b45029c56a413737733ab913fb7e4b5c38c) | [Flask Mega Tutorial: UserLogin](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins), [Flask-Login](https://flask-login.readthedocs.io/en/latest/), [FSWD: SQL Alchemy]:(https://hwrberlin.github.io/fswd/sqlalchemy.html)  |
| Logout and Stop showing Login Page when logged in | [Commit 3](https://github.com/MrGreeeenTea/Dorm-Dine/commit/77aa0b8de6b5b852d1c7b376ae5e998fe4d6aefd) |[Flask-Login](https://flask-login.readthedocs.io/en/latest/) |
| Added Profile Pages, form to edit your own profile with login required | [Commit 4](https://github.com/MrGreeeenTea/Dorm-Dine/commit/474288f1b996c01b2cc617b63314eada9385f5a2) | [Flask-Login](https://flask-login.readthedocs.io/en/latest/) |
|  |  |  |

---

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  |         |                |                                 |                             |
| 02  |         |                |                                 |                             |
| ... |         |                |                                 |                             |
