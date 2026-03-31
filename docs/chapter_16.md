---
title: "Playtesting"
chapter_number: 16
nav_order: 16
layout: chapter
parent: "Part IV: From Prototype to Publication"
---


I hate playtesting. This is an ironic admission from someone who spent years as a musician and had no problem listening to his own material on repeat, picking it apart, reworking arrangements, and playing the same song dozens of times to get it right. Playtesting a wargame should feel the same. It is the same process: you built something, you evaluate it, you revise. But for whatever reason, I find playtesting my own designs tedious in a way that recording my own music never was. I avoid it more than I should, and I have paid for that avoidance with published games that shipped with problems playtesting would have caught.

I mention this because if you find yourself reluctant to playtest, you are not alone. It is a common trait among designers, and it is a dangerous one. The games I am most proud of are the ones that received the most testing. The games I regret are the ones where I convinced myself the design was solid enough to skip the step.

## Why Playtesting Cannot Be Skipped

In Chapter 2, I discussed discontinuing 1987: On to Kaliningrad and 1968: Tet because the foundational research was flawed. Those games had problems that playtesting alone could not fix. But most games do not fail for foundational reasons. Most games fail because individual systems do not interact the way the designer expected, because unit ratings produce the wrong outcomes at the table, because a mechanic that sounded elegant in concept turns into bookkeeping in practice. Playtesting catches these problems. Nothing else does.

Your prototype is a hypothesis. You believe the combat system will produce historical casualty rates. You believe the movement values will create realistic operational tempos. You believe the supply rules will force the same kinds of logistical decisions that constrained the historical commanders. Playtesting is the experiment that tests those beliefs. Some will hold up. Many will not. That is normal and expected. The designer who treats a failed playtest as a setback is missing the point. A failed playtest is the design process working correctly.

## Testing Systems in Isolation

My compromise with my own reluctance to playtest is that I test individual systems in isolation before committing them to the full design. This is faster, less tedious, and catches a large category of problems early.

If I am building a CRT, I set it up with a handful of representative units and run through combat scenarios. I pick attack-to-defense ratios across the full range the game will produce and roll through them repeatedly, tracking the results. Do the casualty rates feel right for the conflict? Are there dead spots on the table where the results are always the same regardless of the ratio? Are there cliff edges where a small change in odds produces a wildly different outcome? You can answer these questions with a CRT, some counters, and twenty minutes of rolling dice. You do not need the full game set up.

The same applies to any subsystem. If you are considering an initiative mechanic, build a small test with a few units and run through the activation sequence. Does the initiative check produce the tempo you want? Does the non-initiative player have enough to do, or are they sitting idle while you resolve activations? If you are designing a supply system, trace a few supply lines on the map and check whether the rules produce realistic constraints. Can units operate too far from their depots? Do the supply costs create meaningful decisions, or are they just bookkeeping?

Testing in isolation will not catch interaction problems between systems. It will not tell you whether the supply rules break when combined with the movement rules under specific terrain conditions. But it will tell you whether each individual system is viable before you invest the time to integrate everything. It is a filter. It catches the worst problems cheaply.

## Finding Playtesters

I find playtesters through Facebook and through my mailing list for Conflict Simulations LLC. This is not a great approach, and I am aware of that. My social media presence is minimal, and my outreach methods are about a generation behind where they should be. But I have been designing games long enough that I have accumulated a network of wargaming friends, many of them through Facebook, and I can usually find people willing to test a new design.

The pool of potential playtesters matters less than the quality of the feedback they provide. You want playtesters who will stress-test your game and tell you things you do not want to hear. Positive feedback feels good. A playtester who tells you the game is great and they had a wonderful time is not helping you improve the design. You need the playtester who tells you the combat system produced a result that made no historical sense on turn three. The one who tells you the setup took forty-five minutes because the instructions were ambiguous. The one who says the supply rules are confusing and they had to invent a house rule to cover a gap.

When you recruit playtesters, make it clear that you want criticism. Tell them you are looking for problems, not praise. Tell them the most useful thing they can report is something that did not work: a rule that was unclear, a mechanic that felt wrong, a setup issue, a result that seemed broken. If they had to invent a house rule to get through the game, you need to know about it. If they hit a situation the rules did not cover and had to make something up, that is a rules gap and you need to close it. If they found a strategy that dominated the game with no counter, that is a balance problem and you need to fix it.

The worst playtest reports are the ones that say "we had fun" and nothing else. The best playtest reports describe specific problems with enough detail that you can reproduce them and take action.

## Blind Playtesting

Blind playtesting is the moment someone plays your game with only the rulebook and no help from you. You are not in the room. You are not answering questions. The rulebook and the components are the only things standing between the playtester and a functioning game session.

This is where rules clarity is tested in a way that no amount of self-editing can replicate. You wrote the rules. You know what you meant. You will read your own rulebook and see the intended meaning because it is already in your head. A blind playtester reads what is on the page, nothing more. Every ambiguity they find is a rules problem. Every question they have to ask is a sentence you need to rewrite. Every situation where they guess at the correct procedure is a gap in your rules.

Blind playtesting is uncomfortable because it exposes problems you thought you had solved. I have had playtesters interpret a rule in a way that was the exact opposite of what I intended, and when I reread the rule, I could see how they got there. The words on the page supported their reading. My intent was irrelevant because my intent was not in the rulebook. This is the most valuable category of feedback you will receive, and you cannot get it any other way.

Blind playtesting happens late in development, after you have done enough internal testing to believe the systems work. Sending out a blind playtest kit before the game is ready wastes your playtesters' time and their goodwill. They will hit mechanical problems that you already know about, and they will lose faith in the project. Wait until the game plays well in your hands before asking someone else to learn it from scratch.

## VASSAL and Digital Playtesting

VASSAL, Tabletop Simulator, and other digital platforms expanded the playtesting pool for wargame designers. Before these tools, playtesting required physical proximity. After the shift to online play, accelerated by COVID, most playtesting networks became geographically dispersed. Digital playtesting is now the default for many designers.

A word of caution before you invest in a VASSAL module or a Tabletop Simulator setup: make sure you have playtesters who will use it. I have paid to have VASSAL modules built for my games, and I have ended up with modules that nobody used. Somewhere between three and eight times this has happened, and I have blocked out the exact count for my own sanity. A module costs money if you are paying someone to build it, and it costs significant time if you are building it yourself. Neither investment is worthwhile if your playtesters do not use the platform.

Before commissioning or building a module, ask your playtesters what tools they use. If your testing group plays on VASSAL, build a VASSAL module. If they use Tabletop Simulator, build for that. If they prefer print and play, send them print and play files. The platform should match your testers, not the other way around.

When digital playtesting works, it is a genuine accelerator. You can schedule sessions across time zones, iterate on the module between sessions without reprinting components, and log game states for later analysis. The speed of iteration is faster because updating a digital module takes less time than reprinting counters and maps. But the tool is only as useful as the people using it.

## Processing Feedback

Not all feedback is equal, and learning to distinguish useful feedback from noise is a skill that develops over time.

The most useful feedback describes a problem. "The combat results on turn four made no sense because a 3:1 attack against a unit in a city produced a defender eliminated result" is actionable. You can go back to the CRT, check the odds, check the modifiers, and determine whether the result is within the intended range or whether something is miscalibrated. "The combat system feels off" is less useful, but it tells you something is wrong even if it does not tell you what. "Change the 3:1 column to produce more retreats" is the least useful type of feedback because it is a proposed solution rather than a problem description. The playtester may be right about the solution, but focus on understanding the problem first. The playtester experienced something that felt wrong. Your job is to figure out what actually caused that feeling and whether the fix they suggest addresses the root cause or just masks it.

Listen for blockers. A blocker is anything that stops a playtest session from continuing: an ambiguous rule that the players cannot resolve, a setup error that puts units in impossible positions, a game state that the rules do not cover. Blockers are the highest priority feedback because they prevent people from playing your game at all. House rules that playtesters had to invent are indirect evidence of blockers. If two different playtest groups invented the same house rule, you have found a gap in your rules that everyone trips over.

Listen for patterns. A single playtester saying the game is too long might reflect their preferences. Three playtesters saying the same thing, without talking to each other, tells you something structural about pacing. One playtester saying the attacker is too strong might be a player who lost. Four playtesters saying the attacker is too strong is a balance problem.

Do not argue with playtesters about their experience. If they tell you something did not work, it did not work for them. You can disagree about the cause. You can disagree about the fix. But their experience at the table is data, and dismissing it because it does not match your expectations is how designers ship broken games.

## Playtesting and Novelty

Testing becomes more critical the more your design relies on original systems. Tried and true wargaming conventions, a standard odds-based CRT, hex movement with terrain costs, IGO-UGO turn structure, carry decades of accumulated testing built into them. Thousands of games have used these mechanics. The failure modes are well understood. If you build your game on established conventions, you can get away with less testing because the individual systems have proven track records.

When you introduce original mechanics, you lose that safety net. A new activation system, a novel combat resolution method, an unconventional approach to supply or command. These systems have no track record. Their failure modes are unknown. They will interact with other systems in ways you have not predicted, because nobody has built this combination before. The only way to discover how they break is to play them until they break.

This is not an argument against innovation. Original mechanics are what push the hobby forward. But they demand more testing than established ones, and you should plan your development timeline accordingly. If your game includes one or two original systems surrounded by conventional ones, the conventional mechanics will not surprise you. The original ones will.

## Case Study: With The Hammer

With The Hammer is the game I am most proud of as a designer, and it is also the game where collaboration during testing changed the design the most.

The game covers the German Peasant War of 1525, a subject I became fascinated with after reading Andrew Drummond's The Dreadful History and Judgement of God on Thomas Müntzer. The conflict is the largest organized popular uprising in European history before the French Revolution, a mass movement of peasants who had decided they had tolerated enough exploitation from their noble landlords. Thomas Müntzer, a radical preacher, became the figurehead of this rebellion, signing his letters "Thomas Müntzer with the Hammer."

The design went through multiple failed prototypes before I found the right framework. I had started by trying to build a Eurogame, inspired by Paladins of the West Kingdom and other designs I admired. But my wargamer instincts kept pushing the prototypes toward literal simulation, and the Eurogame shells felt like re-skins of existing games. Two or three prototypes went nowhere. The breakthrough came when I played Plantagenet in GMT's Levy and Campaign series. That game provided a model of medieval logistics that made sense to me, and I could see how to deconstruct and adapt its DNA into something more approachable for nonwargamers.

The core asymmetry of the design, Peasant leaders preaching and inspiring bands to join the rebellion while Noble armies muster forces and attempt to suppress the uprising through a combination of military force and negotiation, was clear from the start. But translating that asymmetry into a balanced game required extensive iteration during testing.

I brought the design to Fred Serval, who agreed to develop it. Fred's contributions were significant. Peasant leaders gained unique historical abilities: Thomas Müntzer received "Sermon to the Princes," which allows him to attempt to immobilize Noble armies through negotiation. Fred added event cards that alter the rules for a turn or grant abilities to either side. The action allowance system, which determines how many things each side can do per turn, went through multiple revisions to balance the asymmetry between the fast-moving but fragile Peasant leaders and the slower but more powerful Noble armies.

The most instructive moment came during a live discussion on Fred Serval's YouTube channel with Professor Doug Miller, a historian who had been generous in answering my research questions throughout the project. During that conversation, Miller suggested that propaganda markers should have a more meaningful mechanical role. Fred took that suggestion and developed it into a rule that Peasant leaders can only end their movement in locales where propaganda markers are present. That single constraint transformed the game. It gave the Peasant player a logistical puzzle that mirrored the historical challenge of maintaining a rebellion across a dispersed geographic area. You cannot march your leaders wherever you want. You have to preach first, spreading your influence into new areas before your leaders can operate there. The Nobles, in turn, can preach to remove propaganda markers, shrinking the Peasant player's operational space.

This rule did not come from my solo design work. It came from a collaborative discussion during testing, suggested by a historian, refined by a developer, and integrated into a game that was improved by it. The victory point thresholds, the action allowances, the balance between Peasant mobility and Noble military strength, all of these required iteration through testing. The strong core idea was there from the start, but the game that shipped is better than what I would have produced alone.

The lesson is not that you need a developer and a historian on call. The lesson is that playtesting, especially with people who bring different perspectives, surfaces ideas and solutions that a solo designer cannot reach. You see your game from one angle. Playtesters see it from others. A suggestion that sounds minor in conversation, "what if propaganda markers restricted Peasant movement," can solve a design problem you had been struggling with for weeks.

With The Hammer made the front page of BoardGameGeek with a design diary, and it is the design I point to when someone asks what I am most proud of. It is also the design where I was most willing to accept outside input and let the testing process reshape my original vision. Those two facts are not a coincidence.
