---
title: "Rules Writing"
chapter_number: 17
nav_order: 17
layout: chapter
parent: "Part IV: From Prototype to Publication"
---


I have written close to thirty rulebooks, and the early ones were bad. Players had to guess what I meant in places where I thought I had been clear. Rules I considered unambiguous produced questions on BoardGameGeek. Mechanics I thought I had explained generated emails asking for clarification. I knew what the game was supposed to do. I had not learned how to get that knowledge out of my head and onto the page in a form that someone else could follow without help.

A wargame is a miniature algorithm. It has inputs, procedures, conditions, exceptions, and outputs. Your rulebook documents that algorithm, and if the documentation fails, the operator runs the algorithm wrong. The player misapplies a modifier, resolves combat on the wrong column, stacks units in a configuration you never intended, and produces a game state that has nothing to do with the simulation you designed.

You have experienced this as a player. You sit down with a new game, reach a situation the rules do not address, and spend fifteen minutes arguing with your opponent about what the designer meant. You send the designer an email, or post on BGG, or invent a house rule and move on. The designer had an answer when they wrote the rules. They did not get it onto the page.

Rules-writing improves through practice, feedback, and iteration. The skill overlaps with game design but the two are separate disciplines. I know brilliant designers who write terrible rulebooks, and clear rules writers whose games are mediocre. You need both skills, and this chapter is about developing the one that gets less attention.

## The Case System

The SPI case system is the gold standard for wargame rules, and variations of it appear in games from GMT, MMP, Compass, Decision, and every small publisher I am aware of, including my own. If you have played a wargame published in the last forty years, you have read rules organized this way.

The system uses numbered sections and subsections arranged in a hierarchy. Major systems get top-level numbers: 1.0 Introduction, 2.0 Scale, 3.0 Important Concepts, 4.0 Sequence of Play, and so on. Subsections nest beneath them (3.1, 3.2, 3.3) and sub-subsections go deeper (3.1.1, 3.1.2). The numbering gives a permanent address to every rule in the game. A player aid card can say "see 6.1.4" and the player finds that rule without hunting through paragraphs. An errata sheet can say "replace 10.3 with the following" and nobody wonders what is being corrected.

The case system mirrors the structure of the game itself. A wargame turn is a sequence of phases. Each phase contains specific actions governed by specific rules. The rulebook follows that sequence, grouping rules under the phase where they apply. A player working through their first turn reads the rulebook in order and encounters rules in the same sequence they need them. A veteran on their tenth game jumps to a case number and resolves a question in seconds.

The sequence of play appears early in the rulebook because it is the skeleton that the rest of the rules hang on. Once the player knows the order of phases, each subsequent section fills in the details. The SOP tells you what happens and when. The case sections tell you how.

This structure makes sense beyond wargames. Monopoly has a sequence of play: roll dice, move, resolve the space, check for special conditions, pass the turn. So does every board game. Wargames formalize the structure more than most because they carry more moving parts, more exceptions, more situations where the correct procedure is not intuitive. The case system responds to that complexity by imposing order on the rules so the player does not have to impose order themselves.

## Rules-Writing as Technical Writing

A finished rulebook is an exercise in technical and instructional writing. You need different muscles for this than for designing the game, and different muscles than for creative or academic prose.

Technical writing demands precision. A sentence should say one thing, say it clearly, and leave no room for a second reading. When you write "units may not enter enemy-occupied hexes," that statement needs to hold in all cases, or you need to list the exceptions right there. If engineers can enter enemy-occupied hexes under specific conditions, that exception belongs with the movement rule, not four pages later in the engineer section where a player resolving movement will never find it.

Instructional writing demands sequence. The reader needs to encounter information in the order they need it. If a rule depends on a concept defined elsewhere, you either define the concept first or provide a cross-reference. Do not assume the reader has memorized the entire rulebook before applying any individual rule. They are learning your game while they play it for the first time.

The hard part is that you already know how your game works. You designed it. You have played it dozens of times. When you read your own rules, you fill in gaps with knowledge that lives in your head but not on the page. A sentence that reads as clear to you is ambiguous to someone who does not share your mental model. Blind playtesting, discussed in the previous chapter, is the best test of rules clarity. A blind playtester reads only what is written.

A wargame rulebook also carries some academic weight. Your introduction contextualizes the conflict. Your scale section explains why you chose these unit sizes and time increments. Your design notes, if you include them, explain the historical reasoning behind specific mechanical choices. All of this needs to serve the primary job: getting the player from the box to a functioning game session.

## When to Write the Rules

Some designers write comprehensive rules before building a prototype, using the rulebook as a design document that forces them to think through procedures in advance. Others write rules last, once the game is internalized through months of playtesting.

I write rules last. By the time I sit down to write a complete rulebook, I have played the game enough that every system, every interaction, every edge case is something I have encountered and resolved. I keep a bare-bones copy during testing, enough to keep the procedures straight, but the real rulebook comes after the design is finished. You do not waste time writing detailed rules for systems that get cut or reworked during development. You write them once, for the game that exists.

The danger of writing last is that you are writing when you are most blind to your own assumptions. After months inside the design, procedures that are second nature to you may not be obvious to a first-time player. You skip steps because you have internalized them. You use terminology without defining it because the definitions feel so obvious you forget they need stating. I have fallen into this trap more times than I want to count.

Whatever your timing, write as if the reader knows nothing about your game except what you put on the page. Assume they understand wargaming conventions in a general sense. Most wargamers know what a ZOC is, what a CRT does, what stacking means. But they do not know how your ZOC works, what your CRT produces, or what your stacking limits are. The player who has played a hundred wargames still needs you to tell them whether entering your ZOC costs all remaining movement points or just one extra, whether your ZOC prevents retreat or costs a step loss on retreat, whether friendly units negate your ZOC. These implementation details vary from game to game, and you need to spell out each one.

## Calibrating Complexity

Match your rulebook to your game. A simple game does not need to read like the ASL manual. A complex simulation cannot afford to leave out procedures players need.

Approach your player assuming they will not know anything you do not explain. Experienced wargamers still approach your specific game as beginners. The mechanisms may be familiar in concept, but your implementation, your values, your interactions between systems are all new. If your movement system uses terrain costs, list every terrain type and its cost. If your combat system uses modifiers, list every modifier and when it applies. Do not rely on the player deducing anything from general wargaming experience.

At the same time, know your audience. A game aimed at experienced wargamers does not need to explain what a hexagon is. An introductory game might. The tone and detail level should match the complexity of the game and the experience of the intended player.

Separating basic and advanced rules is one of the better techniques for managing complexity in a single rulebook. Core mechanics go in the main body. Advanced, optional, and additional complexity goes in a marked section that players can ignore until they are comfortable with the base game. Sedan 1940 uses this approach. The basic rules cover everything needed for a complete game. The advanced rules add command and control, headquarters, hidden units, and variable artillery results in a self-contained section that tells the player what changes, what new procedures it introduces, and how it modifies existing rules. Players can learn the game in stages rather than absorbing the full system at once.

## Examples of Play

An example of play takes an abstract rule and shows it in action. Specific units, specific terrain, a specific die roll, a specific outcome. The rule tells the player what to do. The example shows them what it looks like. For any mechanic that involves multiple steps, modifiers, or conditional outcomes, one example teaches more than another paragraph of explanation.

Combat resolution is where examples matter most. Walk through selecting the attacking and defending units, calculating the odds, applying terrain modifiers, shifting the column, rolling the die, interpreting the result, applying losses. A player who follows that walkthrough can verify their understanding at each step and then apply the same procedure to their own combats with confidence. Without the example, they are guessing whether they assembled the steps correctly.

Place examples right after the rule they illustrate. Not in an appendix, not at the end of the chapter. The player reads the rule, reads the example, and moves on. Separating the two forces cross-referencing between locations, which is the kind of friction a rulebook should eliminate.

Include as many examples, diagrams, images, and tables as you can produce. A map excerpt showing a combat situation with units, terrain, and modifiers labeled communicates faster than a written description of the same situation. This is an area where I have always been weak. My own manuals lack diagrams and visual aids, a product of limited graphic design ability on my part. If you have the skills or the budget to include visual examples, use them. A labeled diagram of a combat situation will do more for comprehension than the most careful prose you can write.

## Player Aids

A player aid card sits on the table next to the game and holds the information players reach for most often during play: the CRT, the terrain effects chart, the sequence of play, combat modifiers, movement costs. If a player would otherwise flip through the rulebook to find it mid-turn, it belongs on the aid.

A good player aid eliminates rulebook lookups. The player glances at the card, finds the modifier or terrain cost, resolves the action, and keeps moving. A bad one, missing a critical table or carrying wrong values, sends the player back into the rulebook and breaks the flow of the game.

Player aids also matter during playtesting. A playtester flipping through your rulebook to find a modifier during combat is testing your rulebook's navigation, not your game. Give them the reference material on a card and they will spend their time finding problems with the design instead of problems with the index.

Build your player aids early. They will change as the game changes. But having reference sheets from the first playtest forward makes every session more productive.

## Managing Ambiguity

Write your rulebook to be as unambiguous as you can, within reason. You will not anticipate every edge case. You can minimize the common sources of confusion and address the situations most likely to produce arguments at the table.

Scope is the most frequent culprit. A rule says "units may not move through enemy units." Does that apply during retreat? During advance after combat? During strategic movement? If yes in all cases, say so. If exceptions exist, list them with the rule. Every general statement in your rules needs this check: are there situations where the general statement breaks? Address those situations in the text.

Inconsistent terminology causes problems that look like ambiguity but are really carelessness. If you call it "Assault Combat" in one section and "Close Combat" in another, the player cannot tell whether these are two different mechanics or two names for the same one. Pick your terms early, define them in an abbreviations or concepts section, and use them with discipline throughout. The abbreviation table that opens the Important Concepts section of a rulebook is a contract with the reader: these are the terms I will use, and they will mean the same thing every time.

Cross-references tie the rulebook together. When a rule in the movement section interacts with a rule in the combat section, a parenthetical case number lets the player find the related rule without searching. "Units in an EZOC may not use Strategic Movement (see 13.1)" tells the player where to look. Without the reference, they have to scan the entire rulebook for the Strategic Movement rules.

You will not achieve perfect clarity. Every rulebook ships with ambiguities that surface only when thousands of players encounter situations the designer and playtesters never hit. Errata and FAQ documents exist for this reason. But every ambiguity you catch before publication is a question that hundreds of players will not have to ask.

## Other Designers' Rulebooks as a Resource

Other designers' rulebooks are one of the richest and cheapest resources available to you. Every major and minor wargaming publisher offers game rules for free, as downloads on their websites or bundled with VASSAL modules and print-and-play kits. It costs nothing to read them.

Read rulebooks for structure and formatting, not just mechanics. How does a publisher you admire organize their sequence of play section? How do they handle cross-references? How do they format examples of play? How do they present terrain effects? What goes on their player aids? You will find approaches you like and approaches you do not. Both teach you something. The good ones give you models to adapt. The bad ones show you what to avoid.

Pay attention to how different publishers balance completeness against readability. Some rulebooks are exhaustive, covering every edge case at the cost of length and density. Others are concise, covering core procedures cleanly but leaving some situations to player interpretation. The right choice depends on your game, your audience, and how much mechanical complexity you are asking the player to manage.

Reading other rulebooks also exposes you to structural ideas you may not have considered. Layered rules with basic and advanced tiers. Quick-start guides that get players playing before they finish the full rulebook. Extended play examples that walk through an entire game turn. Annotated designer notes that explain why a rule exists. All of these are techniques you can steal. Rules writing does not reward originality of format. If another designer solved a structural problem you are facing, use their solution.

## Case Study: From 1916 to Sedan 1940

My own rulebooks across a decade of publishing show how rules-writing improves through experience, and how the case system supports that improvement when you lean into it.

1916, my game on Verdun, was one of my earliest published rulebooks. It covers a ten-turn operational game at the division level, centered on Administrative Points as the core resource. The case system is present. Sections are numbered. Important Concepts appears early. The sequence of play is laid out. A wargamer can learn the game from it.

But it carries the problems of an early rulebook. The unit descriptions section opens by listing five unit types, then describes seven. The gas rules explain that a roll of 1-3 shifts the CRT one column left (gas blows back at the Germans) and a roll of 4-6 shifts the CRT one column left (gas blows into the French). Read that again. Both results say "left." The intended asymmetry is clear if you already understand the game: 1-3 hurts the attacker, 4-6 hurts the defender. But the text as written says the same thing happens on both results. A reader encountering this for the first time cannot resolve it without guessing or emailing me.

The stacking rules mix different constraints in a single block (same corps, different corps, infantry, non-infantry) that requires careful parsing to untangle. The Administrative Points section does not explain the conceptual framework of the system until much later, in the design notes, where I write that units are "buckets for Administrative Points." That sentence is the conceptual key to the entire game. It belongs in the rules section, not the design notes. A player reading the rules in order does not encounter it until after they have already struggled to understand AP in the abstract.

I knew what I meant. I did not get what I meant onto the page.

Sedan 1940, published several years later, shows what practice does. The abbreviation table at the top of Important Concepts is clean, comprehensive, and lists every abbreviation the player will encounter. Each unit type gets its own numbered subsection with consistent formatting: what the unit is, what values it has, what special rules apply, and a cross-reference to any relevant case number. The sequence of play is laid out and each phase gets its own section, in order, with relevant rules grouped under the phase where they apply.

The basic/advanced split is one of the strongest structural choices in the Sedan rulebook. The advanced rules section opens by telling the player what it adds (Command, Headquarters, Hidden Units, Variable Artillery Results), what changes from the basic game, and states that where the advanced rules conflict with the basic rules, the advanced rules take precedence. That last sentence is small and important. It tells the player which version of a rule governs without ambiguity.

Sedan's combat system is more complex than anything in 1916. It runs dual combat types (Fire Combat and Assault Combat), each with its own table and modifiers. The Assault Combat Table produces compound results: attacker disruption, defender disruption, exploitation allowance, low fuel, low ammo, sometimes combined in a single result. The rules handle this by giving each result type its own numbered subsection under the ACT rules. Attacker disruption is 6.1.4.3.3. Exploitation allowance is 6.1.4.3.4. Low fuel and low ammo is 6.1.4.3.5. A player who rolls a compound result and forgets how exploitation works goes to 6.1.4.3.4 and finds the answer. They do not need to reread the entire combat section. The case system is doing its job.

The design notes in Sedan are tighter than 1916's. Instead of burying the conceptual framework in the back of the book, the Sedan notes focus on specific design choices: why machine gun companies are abstracted into unit ratings, why non-infantry units require Overwatch to use Opportunity Fire, how the German concept of Auftragstaktik influenced the activation structure. These notes enrich the player's understanding of the game. They do not compensate for gaps in the rules.

I did not become a better writer in some general sense between these two games. I learned, through feedback and through hearing players tell me they could not understand rules I thought were clear, that rules-writing takes deliberate effort separate from game design. You test every sentence against one question: can a reader who has never played this game understand what I am telling them to do? If the answer is no, you rewrite the sentence. You do this hundreds of times across the length of a rulebook, and each time you get a little better at writing sentences that pass on the first try.

My early rulebooks generated more errata. My later ones generated less. The case system was there from the start. What improved was my ability to use it: putting the right information in the right place, anticipating the reader's questions, writing with the discipline that technical writing demands. That improvement came from writing rulebooks, shipping them, hearing what confused people, and doing better the next time. You learn rules-writing by writing rules.
