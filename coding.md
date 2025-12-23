---
layout: post
title: Coding
description: Personal coding projects and resume
---
# The DAInfo App (Project Info)
## The Inspiration
I attend Deerfield Academy, a boarding school in Massachusetts. We have an internal web application called DAInfo (it was developed in-house). DAInfo has the following features:

- Student Directory
    - Name
    - Email
    - Photo
    - Birthday
    - Dorm/Room
    - Faculty Advisor
    - Dorm Resident
    - Cocurricular/Coaches
    - Sitdown Table (our family-style meal program)

- Faculty Directory
    - Name
    - Email
    - Phone
    - Spouse
    - Residence
    - Title(s)
    - Departments
    - Cocurricular
    - Sitdown Table(s)
    - Committees
- Sitdown Meal Rosters
    - Faculty
    - Students
    - Waiters (students assigned)
- Cocurricular Rosters
    - Faculty
    - Students
- Attendance (we get “Accountability Points” for commitments missed)
- Grades
- OneCard Activity (internal financial account used on campus)

The web app is ugly, unresponsive, inaccessible, and has an unintuitive interface. The search function does not work on Android, and it is sometimes difficult even to perform basic lookup functions. As a new sophomore, I proposed to the Computer Science club to build a mobile app for DAInfo, but they dismissed the idea as being unrealistic and impractical.

I reverse engineered the login APIs and cookie authentication format and wrote code to scrape basic information. A friend became interested, so we started collaborating through GitHub. Over winter break, winter term, spring break, and most of spring term, we built up a fully functional app. We scraped the independent Dining Hall Menu and Student Bulletin too. We also added search and filter functionality that did not exist on DAInfo, but was possible using some internal DAInfo APIs and other information scraped from DAInfo pages.

- Sitdown rosters could be looked up by table number (as opposed to clicking on a student’s table)
- Information such as Faculty Advisor, Dorm Resident, Sitdown Tables, Cocurriculars, etc were clickable links (as opposed to plaintext)
- Students and Faculty could be filtered by first name (in addition to last name)

![](./assets/maker/daWeb1.png)
![](./assets/maker/daWeb2.png)
*DAInfo Web Application. Note: Links are email mailto links, not links to the faculty member’s profile.*

![](./assets/maker/daInitialLogin.png)
![](./assets/maker/daInitialWeb.png)
![](./assets/maker/daInitialHome.png)
![](./assets/maker/daInitialSearch.png)
![](./assets/maker/daInitialBirthday.png)
*Initial Progress*

![](./assets/maker/daDisplaySearch.png)
![](./assets/maker/daDisplayStudent.png)
![](./assets/maker/daDisplayFaculty.png)
![](./assets/maker/daDisplayCocurric.png)
![](./assets/maker/daDisplayTable.png)
![](./assets/maker/daDisplayAbout.png)
![](./assets/maker/daDisplayAP.png)
![](./assets/maker/daDisplayMenu.png)
![](./assets/maker/daDisplayOnecard.png)
*Finished Application*

## Face Detection
As a live demonstration intended to gain interest for the Computer Science Club at our Annual Club Fair, I developed a simple Python OpenCV face-recognition script trained on image data downloaded from DAInfo, that would automatically add recognized students' emails to an email list with the click of a button. The script worked surprisingly well, notwithstanding the limited training data of one image per student. Due to concerns with the privacy of the students whose images were used to train the model, I was unable to use this program at the Club Fair.

I therefore developed an alternative web application where students could search up their name and click “Join Club” to join the club. It used data from DAInfo. This program was very successful, and students enjoyed the convenience in comparison to the conventional method of using a spreadsheet to collect email addresses. Other clubs, alliances, and student organizations adopted it, and the web app has been in use for two years now.

![](./assets/maker/face1.png)
![](./assets/maker/face2.png)
![](./assets/maker/face3.png)
![](./assets/maker/face4.png)
![](./assets/maker/face5.png)

## Vulnerabilities
In my work reverse engineering and debugging the DAInfo APIs, I discovered a few security vulnerabilities:

- Requesting a faculty member’s PID on the StudentDetails endpoint gives us faculty date-of-births (everything else unique to students is undefined) – Lets students access faculty date-of-birthdays
- The login APIs send passwords as plaintext (not encrypted) – Allows for potential credential theft
- Fetching StudentDetails with random PIDs gives names and date-of-births for all students who ever applied to Deerfield (PIDs are chronologically incremented) – Opens up access to unauthorized data
- “Hidden” input fields in the HTML held sensitive information like a student’s teachers and college advisor – Lets students access unauthorized data
- Endpoints for taking sitdown attendance (some seniors are assigned as row captains) and accessing parent addresses (only parents are allowed to view the parent directory) do not authenticate, so any logged in user (any student) can access those endpoints using the URL – Allows students to edit attendance in certain circumstances and access unauthorized data

## Collaboration with ITS
We presented our work to the Head of ITS, who mentioned an unwritten student app development policy that “prohibited all student developed apps”. Due to our impressive work with the app, however, they modified the policy to allow the publishing of apps that have been approved by ITS. They did not want any personally identifiable data going through the app, however, so they suggested an app that displayed Dining Hall Menu, Athletic Schedules, Student Bulletin Posts, etc. Due to other commitments, our work on this new app never reached completion.

As for the security vulnerabilities I found, ITS mentioned a cybersecurity firm employed by Deerfield to conduct audits that did not find everything that I found. They were grateful for my help and patched the more severe vulnerabilities.

![](./assets/maker/daFutureHome.png)
![](./assets/maker/daFutureBulletin.png)
![](./assets/maker/daFutureTheme.png)

## Accessing Code
Although the code currently does not contain any student/faculty PID, some previous versions did. Moreover, the code exposes information sensitive to Deerfield Academy, and so I cannot make the GitHub repository public. If you would like access to the code, please contact me at zsubhash26@deerfield.edu or zohan.subhash@gmail.com.

Fork of the face recognition code with training images removed: [https://github.com/project-info/face-public]()

![](./assets/maker/daIssues.png)
*Current Roadmap*

## Links/Profiles
- [GitHub](https://github.com/Zo-Bro-23)
    - <a href="https://github.com/Zo-Bro-23?tab=repositories&sort=stargazers">
    <img style="margin: 0px;" alt="total stars" title="Total stars on GitHub" src="https://custom-icon-badges.demolab.com/github/stars/Zo-Bro-23?color=55960c&style=for-the-badge&labelColor=488207&logo=star"/></a>
    - <a href="https://github.com/Zo-Bro-23?tab=followers">
    <img style="margin: 0px;" alt="followers" title="Follow me on Github" src="https://custom-icon-badges.demolab.com/github/followers/Zo-Bro-23?color=236ad3&labelColor=1155ba&style=for-the-badge&logo=person-add&label=Followers&logoColor=white"/></a>
    - <a href="https://github.com/Zo-Bro-23/view-count-badge">
    <img style="margin: 0px;" alt="views" title="GitHub profile views" src="https://view-count-badge.zohan.tech/Zo-Bro-23/profile?color=6b105d&labelColor=913e96&style=for-the-badge&logo=eye&label=VISITORS&logoColor=white"/></a>
- [NPM](https://npmjs.com/~zo-bro-23)
- [LinkedIn](https://linkedin.com/in/zobro23)
- [Fiverr](https://fiverr.com/zobro23)

## Projects
### [ZoAuth](https://github.com/Zo-Bro-23/zoauth)
*Demo live [here](https://demo.zoauth.zohan.tech)!*

- Zero effort OAuth - ZoAuth!
- Extremely easy OAuth with providers such as Google, Microsoft, Facebook, GitHub, Discord, and Amazon
- Get running in minutes!

<iframe width="974" height="548" src="https://www.youtube.com/embed/jWLpqkWkTiQ" title="Introducing ZoAuth" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### [Discord Status Notification](https://github.com/Zo-Bro-23/discord-status-notification)

- Easy configuration with a Discord bot token
- Get notifications on when your friends are online or when their status changes
- Easily enable and disable notifications for certain users
- See details about what device they are online on

### [OBS Voicemeeter Integration](https://github.com/Zo-Bro-23/obs-voicemeeter-integration)

- Plugin that integrates OBS Studio and Voicemeeter Potato
- Voice-controlled scene switching, automatic volume control for each scene, and much more
- <a href="https://github.com/Zo-Bro-23/obs-voicemeeter-integration/releases"><img style="margin: 0px;" title="Downloads - 2189" src="https://custom-icon-badges.demolab.com/badge/2189-custom.svg?color=%23E05D44&logo=download&logoColor=white&style=for-the-badge&labelColor=CE4630&label=DOWNLOADS"/></a>

### [C29](https://github.com/Zo-Bro-23/c29)

- C29 - Configure your Logitech G29!
- Different games require different autocenter and range settings, and C29 allows you to edit these settings on the fly, using controls on your wheel! It even has LED feedback to let you know when your settings have been applied!

### [Population Simulation](https://population-simulation.zohan.tech)

- Can run simulations with billions of individuals to test out hypotheses
- Simulation is based on Hardy-Weinberg Principles
- Extremely useful for building population genetics models
- Built it for doing a Mathematical Modelling lab in AP Bio

### [Writing Stats](https://writing-stats.zohan.tech)

- Get stats about your writing!
- What's your average word length? Paragraph length? What's your writing style?
- Built it for a Rhetorical Analysis assignment in one of my English classes

{% include_relative assets/readme.md %}
