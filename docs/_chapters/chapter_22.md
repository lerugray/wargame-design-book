---
title: "AI and the Designer's Toolkit"
chapter_number: 22
nav_order: 22
layout: chapter
---


This is a chapter I need to write carefully, because the subject generates more heat than light in the wargaming community and in creative communities more broadly. I have strong opinions about AI tools. I use them daily. I have built tools that use them. I also understand why some designers want nothing to do with them, and I respect that position even where I disagree with it. If you are reading this chapter and you have already decided that AI has no place in your design process, skip to the next chapter. Nothing I say here will change your mind, and I am not trying to. This chapter is for designers who are curious about what these tools can do and want an honest account from someone who has used them, made mistakes with them, and figured out how to make them useful.

## What AI Does Poorly

AI is bad at taste. It cannot tell you whether your game idea is good. It cannot tell you whether a mechanic is elegant or clumsy. It cannot look at your combat results table and feel whether the outcomes produce the right tension. It does not know what "right" means in the context of your specific design, because "right" is a judgment that requires historical knowledge, design experience, and an understanding of what you are trying to say with this game. AI does not have an argument. You do.

If you ask AI to generate a game concept from scratch, you will get something generic. If you ask it to design your mechanics, you will get something that functions but lacks personality. If you ask it to write your rules without heavy guidance, you will get prose that reads like it was written by a committee that has never played a wargame. The output looks competent at a glance and falls apart under scrutiny. This is slop, and the wargaming community can spot it faster than most audiences because wargamers are a well-read, detail-oriented group who have spent decades developing strong opinions about what good design looks like.

AI is also bad at knowing when it is wrong. It will present incorrect information with the same confidence as correct information. It will fabricate OOB data, invent historical events, and cite sources that do not exist. If you are not knowledgeable enough about your subject to catch these errors, AI will make your game worse, not better. The designer's historical knowledge is the quality filter. Without it, you are building on sand.

## What AI Does Well

AI is good at tasks where the designer provides the knowledge and the AI provides the labor. Research acceleration is the clearest example. If you are designing a game about a specific battle and you need to cross-reference order of battle data across multiple sources, AI can help you organize and compare that data faster than you can do it by hand. If you have a stack of academic sources and need to find every reference to a specific unit, engagement, or logistical detail, AI can search and summarize faster than you can read.

The key word is "faster." AI does not do research you could not do yourself. It does research you do not have time to do yourself, which for a designer working a full-time job and designing games in whatever hours remain, is the difference between a project that moves forward and one that stalls.

I built a tool called Bookfinder General that searches for, downloads, and extracts text from research books, then lets AI read and summarize the content. The tool exists because I needed a way to get through large volumes of historical material quickly without skipping the research. The AI reads the book. I read the AI's summary. I go back to the original source for anything that matters. The AI is doing the first pass, the equivalent of skimming a book to find the relevant chapters. The historical judgment about what to do with that information remains mine.

AI is also good at generating structured output from unstructured input. If you have a pile of handwritten notes, scattered design ideas, and half-formed mechanics, AI can help you organize that material into something coherent. It will not tell you which ideas are good. It will help you see all your ideas in one place so you can make that judgment yourself.

And AI can generate code. If you need a Monte Carlo simulator to run five thousand games and tell you which fate cards are killing your players, AI can write that simulator in an afternoon. If you want a browser-playable prototype that renders your game state and lets a playtester try your design without printing a single component, AI can build that too. I have done both of these things for AMFIOG, and the tools they produced are things I could not have built on my own. The simulator runs five thousand games per strategy profile and generates statistical breakdowns: win rates, loss reasons, resource flows by turn, dice economy, danger scores for every fate card in the deck. The browser version renders the full game with dice allocation, outsider card interaction, and an event log. These are development tools that would have required hiring a programmer a few years ago. Now they require describing what you want to a competent AI and iterating until it works.

## The Source of Truth Problem

The difference between AI that produces slop and AI that produces useful work is whether you give it a source of truth.

AI left to its own devices will generate plausible-sounding content from statistical patterns in its training data. It will average out the design space and give you something that resembles a wargame the way a composite sketch resembles a face. It is recognizable but has no identity. This is what happens when you ask AI to "design a wargame about Gettysburg" with no further guidance.

AI given a source of truth, your research, your design document, your OOB compiled from primary sources, produces different results. It is no longer generating from averages. It is working from your data, following your constraints, building within your framework. The output still requires your judgment to evaluate, but the starting point is your knowledge rather than a statistical composite of the internet.

I have generated OOBs and rulesets with AI assistance that I would not call slop. The reason they are not slop is that I forced the AI to work from historical sources rather than its training data. With Bookfinder General, the AI reads the actual book before summarizing it. With DevForge, my game development tool, the AI reads your game design document before writing a line of code. The GDD is the source of truth. The AI implements your vision rather than substituting its own. The pattern is the same in both cases: you provide the knowledge, you define the constraints, and the AI operates within them.

This does not make AI infallible within those constraints. It still makes mistakes. It still needs oversight. But the mistakes are different in kind from the slop that comes from unconstrained generation. They are implementation errors rather than conceptual errors, and implementation errors are easier to catch and fix.

## The Ethical Question

Some designers reject AI tools on moral or philosophical grounds. They object to how the training data was collected, to the labor practices of the companies building these systems, to the environmental cost, or to the principle that creative work should be done by humans. I respect these positions. They are held by people I admire in this hobby, and I am not going to tell anyone they are wrong for holding them.

My own position: I do not believe there is such a thing as ethical consumption under capitalism, and I believe this more now than I did before I started working a minimum-wage job full time. The supply chains behind your computer, your software, your printer, your phone, the paper your rulebook is printed on, the shipping that delivers your game, none of it is clean. Refusing to use AI tools is a personal choice, and I have no quarrel with anyone who makes that choice. Framing it as a moral high ground while participating in every other exploitative system that modern commerce runs on is a distinction I do not find meaningful.

For those willing to use AI, the question is whether you use it well or poorly. Used well, with your knowledge as the foundation and your judgment as the filter, it is a force multiplier that lets a solo designer with limited time produce work that would otherwise require a team or remain unfinished. Used poorly, without knowledge or judgment, it produces work indistinguishable from not having done the work at all. The tool does not determine the quality. The designer does.

## What AI Gave Me Back

The practical argument for AI tools in wargame design is about what becomes possible when time is no longer the bottleneck.

I burned out around 2020. The publishing company was struggling, my personal life was in disarray, and game design, the thing I had built my identity around, was the last thing I had energy for. For several years I did not design anything meaningful. The ideas were still there. The desire was still there. The time and energy were not.

AI tools changed that equation. I can do in an evening what used to take a week. Research that required days of reading can be surveyed in hours. A prototype that required learning a programming language or hiring a developer can be built in a conversation. A Monte Carlo simulation that would have been beyond my technical ability can be described, built, tested, and revised in an afternoon. The constraint that kept me from designing, not having enough hours in the day while working a full-time job, became manageable.

That matters more than the tools themselves. I am designing again. The creative part of my life is functioning again after years of dormancy. A designer who had run out of time found a way to get it back.

To give you a sense of scale: in less than a month, while working fifty hours a week at a day job, I produced or made significant progress on the following projects using AI tools:

- **A Mighty Fortress Is Our God** — the solitaire siege game discussed in the previous chapter, including its Monte Carlo simulator and browser-playable prototype
- **Kreuzfeuer** — a Reformation-era CRPG built in Godot, set in the same period as AMFIOG, a spiritual successor to Microprose's Darklands with procedural world generation, SRPG combat, and a faction system driven by the German Peasants' War and the Siege of Munster
- **Prigozhin's March of Justice Digital** — a Rust-based digital adaptation of my board game on the 2023 Wagner Group mutiny
- **Death of an Empire** — a Franco-Prussian War digital wargame with command asymmetry and fog of war
- **Sandkasten** — an open-source tactical wargame simulation inspired by Command: Modern Operations, with NATO symbology, radar detection, fog of war, anti-ship missile combat, and an AI-driven InfoWar feed that generates simulated media coverage of in-game events
- **Auftragstaktik** — an OSINT tactical terminal that tracks live frontlines, aircraft transponders, ship positions, air defense envelopes, and conflict events across eleven theaters, with auto-translated Telegram feeds from military blogs and a historical mode covering 140,000 archived conflict events from 1989 to 2023
- **DevForge** — a game development tool built around what I call idea-driven design, the principle that anyone with a strong idea and a clear design document can develop a digital or analog game with AI assistance
- **Bookfinder General** — the research tool discussed earlier in this chapter, and used to compile research for several appendices in this book

None of these are finished. Several are in early stages. The point is not that AI let me ship ten products in a month. The point is that a year ago, I was shipping zero. The bottleneck was never ideas or ambition. It was time and energy, and AI tools compressed the labor enough that projects started moving again.

## Case Study: A Mighty Fortress Is Our God and the Long Road Through AI

AMFIOG had been stuck in my head for over a year before AI got involved. I had notes. I had research on the Munster commune, the siege, the Anabaptist movement, the political and religious dynamics. I had the core idea: a solitaire game about managing a besieged commune, resource management under pressure, the slow constriction of a siege. I knew what I wanted the game to feel like. I could not figure out how to make the pieces fit together mechanically.

At some point, exasperated, I dumped all my notes into a conversation with ChatGPT and asked it to help me find the connective tissue. I told it the game should work as a State of Siege and euro hybrid. It suggested structural approaches that I felt stupid for not thinking of myself: the dice pool as a shrinking resource, the outsider queue as a spatial-economic system, the fate deck as a narrative driver that interacts with the mechanical state. The AI did not design the game. It saw connections in my own notes that I could not see because I was too close to the material.

The experience was not smooth. I had no idea how to work with AI at that point. My chat history was stuck in a buggy ChatGPT window. Conversations grew too long and the AI started forgetting context, contradicting earlier decisions, losing track of the design. It became a nightmare of trying to extract useful information from a deteriorating conversation. I figured out how to pull what I needed out of the text and how to work with command-line tools, which led me to Claude Code, where I could work with my original notes cleanly, maintain context across sessions, and continue development without fighting the tool.

Trial and error. That is the honest summary. The AI was useful from the beginning, but I was bad at using it, and the early tools were bad at maintaining coherence over long conversations. Both of those problems improved with time and practice. The design moved from a pile of notes to a functional prototype with a Monte Carlo simulator, a browser-playable version, and a rulebook that is further along than anything I have produced in years.

Being no longer too burned out to create again matters more than any specific tool. But the tools removed enough friction that designing within the constraints of a full-time job, limited energy, and no budget became realistic again. For a designer in that situation, and there are more of us than the hobby likes to acknowledge, AI is worth learning to use well.
