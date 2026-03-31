---
title: "Organization and Version Control"
chapter_number: 18
nav_order: 18
layout: chapter
---


I am an organizational mess. I have been an organizational mess for the entire time I have been designing wargames, and I am aware that this is a problem, and I have not fixed it. What I have done is find a tool that compensates for it well enough that my projects ship on time more often than they do not. That tool is Basecamp, and I will talk about it and its alternatives in this chapter. But the tool is secondary to the principle, which is this: you need a system for tracking your files, your versions, and your communications, and you need the discipline to use it. The specific system matters less than having one at all.

I am telling you this because all three of those things have happened to me, and the case study later in this chapter describes the worst instance in detail.

## The Problem

A wargame in development generates a lot of files. Map drafts in multiple versions as you revise terrain and hex layouts. Counter sheets revised with every unit rating change. An OOB spreadsheet that feeds those counter sheets. A rulebook that goes through dozens of revisions between first draft and publication. Charts and player aids that need to match the current rules. Playtest notes from multiple testers. Correspondence with your developer, your artist, your printer. VASSAL module files if you are building one. All of this accumulates.

Each file changes over the life of the project. The map you sent your artist in January is not the map you playtested in March, because you moved a victory hex and added a river crossing. The OOB you finalized in February lost three units in April after playtesting showed they unbalanced the game. The rulebook exists in at least four versions: the one you sent to playtesters, the revision after their feedback, the one you sent to your developer, and the one your developer sent back with changes.

Without a system for tracking which version is current, you will send the wrong file to someone who matters. Your artist produces counters from an outdated OOB. A playtester spends an evening with a superseded rulebook. A printer manufactures maps with wrong terrain. Each of these costs time, money, goodwill, or all three.

## What a System Needs to Do

Your organizational system needs to handle four things.

**File storage with version history.** You need to find the current version of any file in your project and look at previous versions when something goes wrong. Cloud tools like Google Drive, Dropbox, and Basecamp keep revision histories automatically. If you work locally, you need a naming convention that makes the current version obvious: "Sedan1940_Rulebook_v3.2.pdf" where the version number increments with each revision. Whatever convention you pick, stick to it across the entire project.

**Collaboration and sharing.** Your developer, artist, playtesters, and printer all need access to the right files. Your artist needs the current OOB spreadsheet and counter layout specifications. Your playtesters need the current rulebook, charts, and map. Your printer needs final production files. A shared workspace where you control access prevents the wrong person from grabbing the wrong file.

**Task tracking and communication.** When your developer sends back a revised rulebook, you need to know what they changed and why. When a playtester reports a problem, you need to track whether you addressed it. Email works when two people are involved. It falls apart at five or six, because conversations fragment across threads and nobody can reconstruct who said what.

**Backup.** Hard drives fail. Cloud services have outages. Your project files need to exist in more than one place. Cloud storage handles this by default. If you work locally, back up to a second drive or cloud service periodically. Losing a month of work on a counter sheet to a dead hard drive is preventable.

## Tools

I use Basecamp. It costs fifteen dollars a month, which I justify because it makes all four of the above requirements easy without me having to think about any of them. I organize each game as its own project in Basecamp. Files go in the file storage. Conversations happen in message boards. Task lists track what needs doing and who is doing it. My developer, my artist, and my playtesters all have access to the project and can find what they need without me acting as a file-distribution service.

Basecamp is not the only option and may not be the best option for your situation. The free alternatives cover the same ground with different trade-offs.

**Google Drive** gives you file storage with version history, sharing with permissions, and the ability to collaborate on documents in real time. Google Sheets is where most of my OOB work happens regardless of what project management tool I use. The revision history in Google Docs and Sheets lets you roll back changes and see who changed what. For a solo designer or a designer working with one or two collaborators, Google Drive may be all you need.

**Dropbox** handles file storage and sharing well. Its version history lets you recover previous versions of files. It lacks built-in task tracking or discussion tools, so you would need to supplement it with email or a messaging platform for communication.

**Trello**, **Notion**, and similar tools provide task tracking and project organization. They are free or cheap at the scale a wargame designer needs. They can store files but are not built primarily as file storage systems, so you would pair them with Google Drive or Dropbox for the files and use the tool for task management and communication.

**Git and GitHub** handle version control with a precision that none of the above tools can match. If you are comfortable with command-line tools or learn to use a graphical Git client, Git tracks every change to every file in your project, lets you compare any two versions, and makes it straightforward to collaborate with others. The learning curve is steep for someone who has never used version control software. I would not recommend it as your first organizational tool unless you are already technical. But if you are comfortable with it, it is the most robust option for tracking file versions.

Do not keep your rulebook in Google Drive, your OOB in Dropbox, your playtest notes in email, and your task list on a sticky note. Put it all in one place. When everything lives in a single system, you know where to look. When it is scattered, you spend time searching instead of designing.

## Naming Conventions and Folder Structure

If your organizational tool does not handle version tracking for you, you need naming conventions that make the current version of any file obvious at a glance.

Include the project name, the file type, and a version number in every filename. "1864_Rulebook_v12.1_Final.pdf" tells you what game, what file, and what version. "Rulebook_new_FINAL_v2.pdf" tells you nothing useful except that someone has lost control of their naming scheme.

Be honest about the word "Final." A file named "Final" that gets revised becomes "Final_v2" which becomes "Final_v2_ACTUAL" which becomes a naming disaster you have seen on your own hard drive and someone else's. Use version numbers. They do not drift.

Organize your project folder by file type: a folder for maps, a folder for counters, a folder for rules, a folder for playtest feedback, a folder for correspondence. Within each folder, the naming convention keeps versions straight. When you need the current counter sheet, you go to the counters folder and grab the highest version number. When your artist needs the current OOB, you point them to the OOB folder and tell them the version number.

Date-modified sorting is a fallback, and I use it more than I should. Sorting files by date and grabbing the most recent one works until you have two files modified on the same day, or until you open an old file to check something and its modification date updates. Explicit version numbers are more reliable. I know this and I still default to date sorting half the time, which is why I pay for Basecamp to handle it for me.

## The Production Pipeline

Organization becomes critical when your game moves from development into production. During development, version errors are recoverable. You send a playtester the wrong rulebook, they tell you something seems off, you send the right one.

During production, version errors cost real money. Your counter artist works from the OOB spreadsheet. If they use an outdated version, the counters ship with wrong values and you do not catch it until the proof arrives. Your map artist works from your latest draft. If that draft predates your last terrain change, the published map has incorrect terrain. Your printer manufactures whatever files you send them. Wrong files in, wrong components out.

Each handoff in the pipeline is a point where a version error can enter the process. Counter manifests need to match OOBs. Map files need to match the latest terrain rulings. Rulebook versions need to incorporate all playtest changes. Player aids need to match the current rules.

A checklist before each handoff catches these. Does the counter sheet match the OOB? Does the player aid match the rulebook? Does the map reflect the latest playtest revisions? Fifteen minutes of verification saves weeks of rework.

## Case Study: 1864: On to Jutland!

1864: On to Jutland!, my game on the Second Schleswig War, is the clearest example in my catalog of what happens when the production pipeline breaks down.

The game itself came together well. It started as one of the more complicated designs I had made, using an in-depth system of operational movement followed by tactical combat inspired by Frank Chadwick's GDW Crimea game. That system would have added hours to playtime, which was the opposite of what the 2140 series is trying to do, so I scrapped it and rebuilt the game around a simpler framework. The perpetual combat mechanic, where players can keep attacking as long as they have units adjacent to the enemy but disrupt themselves after the second assault, was one of the ideas I salvaged from that earlier version. The final game plays quickly and the system works.

The production side did not go as smoothly. 1864 shipped to customers with a playtest map and half-finished counters. Not a pre-production proof. Not an early review copy. The actual retail product that people paid for arrived with components that were not final.

I had to replace components for the customers who received those copies. For a small publisher like Conflict Simulations LLC, replacement costs come out of the margin that was supposed to make the game worth producing. It also costs credibility. A customer who opens a new game and finds playtest-quality components does not think "organizational mistake." They think "this publisher does not care about quality." You do not get to explain the circumstances.

The wrong files went to the printer. Somewhere between the finished production files and the print order, an older map and an incomplete counter sheet were substituted for the final versions. Whether that happened on my end or the printer's matters less than the fact that no verification step caught it before the games were manufactured and shipped.

A checklist would have prevented this. Open the map file, confirm it matches the rulebook's terrain descriptions. Open the counter sheet, cross-reference it against the final OOB. Check the player aids against the current rules. Fifteen minutes. Skipping those fifteen minutes cost me money, customer goodwill, and weeks spent sorting out replacements.

I learned from this. My subsequent games have not had the same problem, in part because I got better at verifying files before sending them, and in part because Basecamp gives me a single location where the current version of every file is clearly identified. When I send files to a printer now, I pull them from Basecamp rather than hunting through my local hard drive for the most recent version. The tool compensates for my weakness without fixing it. I still default to sloppy habits when I am not paying attention. But a system that makes the right behavior easier than the wrong behavior is often enough.

## Discipline Over Tools

Tools are concrete and easy to recommend. Using them consistently is the hard part. Every organizational system works when you set it up. The question is whether you maintain it under pressure, when you are focused on fixing a broken CRT and updating a version number feels like busywork.

I am not good at this. My natural tendency is to save files with vague names, forget to update version numbers, and rely on date sorting to find the current file. Basecamp compensates, but only because I have made it the default place where project files live. If I kept some files in Basecamp and some on my desktop, the system would collapse.

Pick a system. Use it for everything. When you feel the pull to save a quick revision to your desktop instead of the shared workspace, resist. When you want to name a file "rules_new.pdf" instead of "1864_Rulebook_v12.1.pdf," take the extra ten seconds. The discipline is harder than choosing the tool, and it matters more. Nobody who buys your game will see your design process. They will see the box they opened, and the components inside need to be the ones you intended to ship.
