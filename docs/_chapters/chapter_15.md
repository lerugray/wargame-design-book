---
title: "From Concept to First Prototype"
chapter_number: 15
nav_order: 15
layout: chapter
---


The preceding thirteen chapters covered the anatomy of wargames in detail. Scale, time and space, orders of battle, movement, combat, sequences of play, subsystems, specialized domains, card systems. You now have a vocabulary for the components that make up a wargame and a sense of the design decisions each component demands. This chapter is about sitting down and building one.

I cannot give you a formalized process for this. Every designer I know works differently, and every designer I know has tried to formalize their own process at some point and failed. You are going to start with whatever excites you most about your design, and that starting point will be different for every project and every designer. Some designers begin with the map because visualizing the theater is what orients them. Others start with the OOB because they want to see the forces before making any other decisions. Some start with a single mechanic, a combat system or an activation structure, and build everything else around it. All of these are valid entry points. None of them is the correct one.

I can walk through the minimum set of things you need before you can push cardboard, and then be honest about how I work, including the parts of my process that are mistakes.

## The Minimum Viable Prototype

Before you can play a single turn of your game, you need five things.

A map. It does not need to be beautiful. It does not need to be finished. It needs hexes, terrain, and enough geographic accuracy that the spatial relationships between forces hold up. A hand-drawn map on graph paper works. A quick map thrown together in GIMP works. If you are doing area control or point-to-point, you need locations and the connections between them. The map will change. Do not invest significant time in making it look good at this stage.

Counters. You need physical pieces to push around the map. Blank counters are available online from various hobby suppliers. The old-school technique, and one that still works, is to print your counter sheet on paper, glue it to a piece of cardboard, and cut them out. This produces functional double-sided counters for almost no cost. If you are testing digitally through VASSAL or Tabletop Simulator, you can skip physical counters, but I find that pushing real cardboard teaches you things about your game that digital testing does not. Moving pieces, stacking them, flipping them, picking through a pile to find the one you need. These interactions tell you whether your game has too many pieces, whether the information on the counters is readable, whether the stacking limits feel right.

A sparse rulebook. Not a finished rulebook. Not a comprehensive rulebook. A document that contains the sequence of play, the core movement and combat procedures, and enough explanation that you can run a turn without stopping to invent rules on the fly. Write this as a reference, not as a teaching document. You are the only person who needs to understand it at this point. It will be incomplete. You will fill in gaps as you play. That is the purpose of the exercise.

Charts. Whatever your game needs to resolve its procedures. A CRT, a terrain effects chart, a turn record track, a combat modifiers summary. Print these on separate sheets so you can reference them during play without flipping through the rulebook.

Dice, cards, or whatever randomization your game uses. If your game uses a card deck, you will need at least a rough version of that deck. Index cards with handwritten descriptions are sufficient for early testing.

That is the minimum. Map, counters, sparse rules, charts, and randomizers. Everything else is refinement. Do not write a full rulebook before you have played a single turn. The rulebook exists to document what you have tested, not to prescribe what you are about to test. I have watched designers spend months writing detailed rulebooks for games they have never played, and in every case the first playtest invalidated half of what they wrote.

## The Design Document

I have never made a design document for any of my analog games. This is a mistake.

I have designed close to thirty published wargames without a formal GDD, and I got away with it because I tend to start projects with strong opinions about what the game should feel like and what it should not try to be. Those opinions live in my head, and they survive the development process because I am the one making every decision. But there have been projects where scope crept in slowly, where a mechanic that seemed like a natural extension of the design turned into a subsystem that dragged the game in a direction I did not intend. A design document would have caught those moments earlier.

I started using design documents for digital projects I am working on, and the difference is noticeable. A written thesis, a clear statement of what the game is trying to do, keeps the project from expanding past its boundaries. It does not need to be elaborate. A page is enough. Your thesis boiled down to its mechanical representation: what is the central question the player is answering, what scale and scope serve that question, what systems are necessary and which are not. Write it before you build anything. Refer to it when you are tempted to add a subsystem. If the subsystem does not serve the thesis, it does not belong in the game.

I did not do this for most of my career, and I paid for it in extended development cycles and features that got cut after consuming weeks of design work. You can get away without a design document if you have strong enough instincts and you are willing to rework things when they drift. But having one is better than not having one. I am certain of that now.

## How I Work

My process is not the recommended process. It is the process I have settled into after a decade of designing games, and it has strengths and weaknesses that I am aware of but have not fully corrected.

I tend to start with the map and the OOB. I want to see the theater and the forces before I make mechanical decisions. Looking at a map of the campaign area and seeing where the armies were positioned, where the terrain features create natural defensive lines, where the roads and rail lines run. That orients me. The OOB does the same thing from the other direction. Seeing the specific formations involved, their relative strengths, how they were organized. That tells me what scale feels right and what level of detail the game needs.

Once I have a rough map and a rough OOB, I start thinking about systems. I tend to have strong ideas about what the core mechanic should be, some notion of how activation should work or what the combat system needs to capture. Those ideas come from the research, from the specific qualities of the conflict that make it worth simulating. I develop those systems, test them against the map and OOB, and then write the framework around them. Rules that do not make sense get cut. Systems that add overhead without adding decisions get cut. I prune after building, rather than designing a minimal framework from the start.

This approach has a disadvantage that I should be honest about. If I design the OOB and then later change a mechanical rule that affects how unit ratings work, the entire OOB needs reworking. This has happened to me more than I would like.

We Were Not Cowards, my Imperial Bayonets series game on the Battle of Sedan in 1870, went through four or five complete reworkings of the strength and initiative ratings over the course of development. That game took years to finish, in large part because the combat system, which I believed was well designed and did not want to change, was not producing the outcomes I wanted with the original unit ratings. The system was sound. The numbers feeding into it were not. Each time I adjusted the numbers, I had to recalculate every unit in the game, cross-reference against the historical data, playtest the new values, and determine whether the results matched what I was looking for. Multiply that by four or five iterations and you understand why the project took as long as it did.

A designer who writes rules first and builds the OOB to fit those rules avoids this problem. The trade-off is that their OOB may feel forced, shaped by mechanical requirements rather than historical research. Neither approach is wrong. Both have costs. I am comfortable with my approach because reworking OOBs is something I know how to do, but I would not claim it is the more efficient method.

## Tools

You do not need expensive software to design a wargame. The tools that matter are the ones that let you create, iterate, and share your work without friction.

**GIMP** is an open-source image editor that does everything Photoshop does for the purposes of wargame design, and it costs nothing. I use it for map drafts, counter sheets, and charts. The learning curve is real but manageable, and for a designer who will be creating and revising visual assets across the entire life of a project, learning GIMP is time well spent.

**Google Sheets** is where OOBs live, where CRTs get built, and where combat math gets tested. Spreadsheets are the backbone of wargame design whether you realize it at the start or not. Every unit rating, every probability calculation, every strength point total will end up in a spreadsheet at some point. Google Sheets has the advantage of being free, accessible from any machine, easy to share with playtesters and collaborators, and easy to hand off to an artist when the time comes. If your OOB is in a Google Sheet, your counter artist can work directly from the source data instead of translating your handwritten notes.

**VASSAL** is valuable for playtesting and prototyping, but it requires specialized knowledge to build modules. If you are comfortable learning the module editor, VASSAL lets you playtest your game digitally, share the module with remote playtesters, and iterate on the map and counters without reprinting physical components. The barrier to entry is not trivial. Building a VASSAL module for even a simple game takes time, and debugging module behavior can consume hours. But if your playtesting network is geographically dispersed, and in 2026 most playtesting networks are, VASSAL is worth the investment.

**Tabletop Simulator** fills a similar role to VASSAL with a different set of trade-offs. It is more accessible to non-wargamers and provides a three-dimensional environment that some playtesters find more intuitive. The downside is that it is a commercial product, your playtesters need to own copies, and the scripting required for automated game functions is more complex than VASSAL's module tools.

**Basecamp** or similar project management tools become useful when you are working with a group. If you have a developer, an artist, and playtesters all contributing to the same project, you need a shared space for files, discussions, and task tracking. Basecamp is what I use. It is a paid tool, but there are free alternatives. The specific tool matters less than having a system. When multiple people are working on the same game, files get lost, conversations happen in scattered email threads, and nobody is sure which version of the rulebook is current. A shared project space prevents that.

**Pen and paper.** I keep a notepad next to me whenever I am playtesting. Ideas come up during play that you will forget if you do not write them down. A mechanic that feels clunky, a unit that seems too strong, a terrain feature that does not work the way you expected. Write it down in the moment. Review your notes after the session. This is the simplest tool on the list and one of the most important.

## Print and Play

When your prototype reaches the point where other people need to play it, print and play is the easiest distribution format.

A print-and-play kit is a set of files that a playtester can download, print on their own printer, and assemble into a playable game. The map prints on standard paper, possibly taped together if it spans multiple sheets. The counters print on a sheet that the playtester cuts out and mounts on cardboard. The rules and charts print as separate documents. Everything a playtester needs to play the game fits in a folder of PDFs.

This is simpler than manufacturing and mailing physical playtest kits, and it scales to any number of playtesters. You email the files, they print and assemble, and you are testing. The trade-off is that your playtesters need to do the assembly work, which means you need to include clear instructions for how to put the kit together. Which pages to print, how to mount the counters, how to assemble the map if it spans multiple sheets. Do not assume any of this is obvious. Playtesters who receive a pile of unmarked PDFs with no instructions will not playtest your game. They will set it aside and forget about it.

Keep your print-and-play files organized and version-numbered. When you update the counter sheet because you changed unit ratings, the old version needs to be clearly superseded. Playtesters working from outdated components will give you feedback based on values you have already changed, which wastes their time and yours.

## Conceptual Work vs Physical Prototype

There is a distinction between the conceptual design of a game and the physical prototype, and it is worth being explicit about the difference because new designers sometimes conflate them.

The conceptual work, deciding on scale, working out the core systems, researching the OOB, drafting the sequence of play, thinking through how the mechanics interact, can happen in a week. Not a finished design, but enough of a framework that you know what game you are building and what its core systems look like. This is desk work. Reading, thinking, scribbling in a notebook, building a spreadsheet. It does not require any physical components.

The physical prototype, a map you can lay on a table, counters you can push, charts you can reference, takes longer. Weeks to months, depending on your skills and the complexity of the game. If you are comfortable with image editing, counter layout, and the physical craft of cutting and mounting components, you can move faster. If those skills are new to you, expect a learning curve. The prototype does not need to be beautiful, but it needs to be functional, and "functional" means readable counters, a legible map, and charts that contain the right information. Building all of that takes time.

Do not let the prototype phase intimidate you into staying in the conceptual phase forever. A game that exists only as notes and spreadsheets is not a game. It is an idea. The idea might be brilliant, but you will not know until you play it. Push yourself to build the prototype even if it looks rough. You will learn more from one play session with ugly cardboard than from another month of conceptual refinement.

## Case Study: Prigozhin's March of Justice

Prigozhin's March, discussed in detail in Chapter 6, illustrates what happens when the subject itself is small enough to compress the entire design process. The event lasted thirty-six hours. The forces were a handful of units on a linear route. The central question was obvious from day one. I had a working prototype within days, not weeks.

What made this project different from my usual workflow was the speed of iteration. The game was small enough that I could play a full session in a short sitting, identify a problem, adjust a value, and play again immediately. That rapid cycle is difficult to sustain on a larger game, but it worked here because the scope allowed it. Two or three turns told me whether a change improved things or made them worse. I also playtested early and heavily, something I am usually reluctant to do with larger designs where I want the systems more developed before I subject them to outside evaluation.

If you are designing your first game, Prigozhin's March is the model. A game with a narrow geographic scope, a limited number of units, and a compressed time frame will teach you more about design per hour of effort than an ambitious operational game covering an entire campaign.
