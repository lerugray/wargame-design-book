---
title: "Sequence of Play"
chapter_number: 10
nav_order: 10
layout: chapter
parent: "Part II: Core Systems"
---


A sequence of play is an algorithm. You write a set of ordered instructions that allow at least one or more human beings to run the simulation you have designed. A player opens your rulebook and reads "Phase 1: Weather Determination. Phase 2: Supply Check. Phase 3: Movement. Phase 4: Combat. Phase 5: Exploitation." That player is reading a program written in natural language. The sequence tells them what to do, in what order, and when control passes from one player to the other. If the algorithm is clear, the game runs. If it is ambiguous or poorly ordered, players will spend more time arguing about procedure than making decisions about the battle.

The sequence of play is one of the more useful contributions wargaming has made to game design as a whole. Board games benefit from clear turn structure, but wargames formalized it into something closer to a flowchart. A good SOP lays out how the game works in practical terms. New players read it to understand what they are going to do on their turn. Experienced players reference it when a timing question comes up mid-game. Every other system in your design, movement, combat, supply, command, plugs into the sequence of play. You build the SOP and hang everything else off it.

## IGO-UGO

The most common sequence structure in wargaming is IGO-UGO: one player completes their entire turn, then the other player completes theirs. The phasing player moves all their units, resolves all their combats, handles administrative tasks, and passes control. The non-phasing player watches, may roll dice when required, and waits.

IGO-UGO has dominated the hobby since SPI and Avalon Hill established the conventions, for good reason. It is easy to learn, easy to teach, and easy to develop for. You as the designer know when each system activates because the sequence is linear and predictable. Movement happens in the movement phase. Combat happens in the combat phase. No ambiguity about timing. For the player, IGO-UGO provides a complete picture of the situation before they commit to action. You see where every enemy unit sits, calculate your odds, and execute your plan.

Most of my games use IGO-UGO to some degree. The World Undone series, Imperial Bayonets, the LCOS games, all of them give one player a full turn before the other player acts. I keep coming back to IGO-UGO because it works. The structure is transparent, the timing is unambiguous, and I spend my design effort on the systems rather than the meta-structure holding them together.

The weakness is passivity. The non-phasing player has nothing to do for extended stretches. In a complex game with a large OOB, one player's turn can take thirty minutes or more. The other player sits there. Competitive players use that time to study the board. Casual players disengage. This is a real problem, and it is one reason designers have explored alternatives.

The other weakness is predictability. The phasing player knows they will complete all their movement before any combat occurs. They know no enemy unit will interrupt their plan. That certainty is unrealistic. Real commanders did not get to move every unit on the battlefield before the enemy responded. But the abstraction works because the turn represents a block of time during which both sides were acting at once, and IGO-UGO is a practical way to resolve that simultaneity in a sequential format.

## Impulse Activation

Impulse activation breaks the turn into smaller segments. Instead of one player moving everything and then fighting, each player activates a portion of their force, a single unit or a formation or a stack, and then control passes. The turn becomes a series of alternating impulses until both players have activated everything or chosen to stop.

The benefit is engagement. Neither player sits idle for long. You activate a unit, I activate a unit. The back-and-forth keeps both players involved. In an IGO-UGO game, you plan and then execute. In an impulse game, the situation changes between each of your activations, so you are recalculating after every opponent move.

Impulse activation also introduces cost. If activating a unit costs something, action points, command tokens, a card from your hand, then you face decisions about what to activate and in what order. Do you move that formation now or save the activation for a reaction later? IGO-UGO does not ask that question. Every unit activates for free during its phase.

The design challenge with impulse systems is pacing. If each impulse involves a single unit, the game might crawl. If impulses involve entire formations, you are back to something close to IGO-UGO with extra steps. A tactical game where individual squads activate one at a time feels right. An operational game where individual divisions activate one at a time gets tedious if there are forty divisions on the map (PCS is guilty of this sometimes). Find the right granularity for your subject.

## Chit Pull

Chit pull deserves more attention from designers than it gets. The basic mechanic: place activation markers for each eligible formation into an opaque cup. Draw one at random. That formation activates. Draw the next. Continue until the cup is empty.

Chit pull simulates the unpredictability of conflict better than any other structural mechanic I have used. You cannot rely on a specific formation to activate when you need it. Your plan requires the 2nd Panzer Division to move before the enemy infantry digs in, but its chit might be the last one drawn. That uncertainty changes decision-making at every level. You cannot build a plan that depends on precise sequencing because you do not control the sequence. You have to build plans that work across a range of activation orders, which is closer to what real commanders face.

In Sedan 1940, I built a non-linear chit-pull driven sequence of play. Your activation chit gets pulled and you can move, fire, assault, enter overwatch, or do whatever else the rules allow. No fixed phase structure within the activation. The game was inspired by John Tiller's Panzer Campaigns PC series, which I admired for its fluid turn structure, but I combined that fluidity with chit pull to add the unpredictability that a deterministic PC game could not provide. The 1940 campaign in France was fast, disorienting, and depended on which commanders seized initiative at the right moment. The activation system produces that tempo without scenario rules having to force it on top of providing a hook for replayability and solitaire players.

I would encourage designers to explore chit pull across many different systems and subjects. At tactical scale, squad-level activation creates the chaos of small-unit combat. At operational scale, formation-level activation models the friction of coordinating a multi-corps offensive. At strategic scale, theater-level activation captures the competing priorities of a high command that cannot do everything at once. The mechanic is adaptable and intuitive. It produces uncertainty that makes games replayable without adding rules overhead.

## A Note on Card-Driven Games

Card-driven games are sometimes discussed as a separate category of activation system. That framing is misleading. A CDG can be IGO-UGO, impulse-based, or use a form of chit pull depending on how the cards function. The cards are a resource and randomization layer that sits on top of one of the activation structures discussed above. Mark Herman's We the People and its descendants use cards for both operations and events, but the underlying turn structure varies from game to game. CDGs deserve their own chapter, and I will get to that later.

## Reactions and Opportunity Actions

The most effective way to solve the passivity problem in IGO-UGO games is to give the non-phasing player things to do during the phasing player's turn.

Reactions, opportunity fire, interceptions, and reserve activations all serve this purpose. They break the normal sequence of play in controlled ways. The defending player responds to threats as they develop rather than waiting for their own turn. Real defenders did not sit motionless while the enemy maneuvered. They fired at approaching troops, repositioned reserves, and attempted to disrupt attacks before they materialized.

In Mons 1914, the non-phasing player can conduct opportunity fire against units moving within range. The BEF's rifle fire in August 1914 was so rapid and disciplined that a popular trope is that German commanders believed they were facing machine guns (though that could just be a bit of historical propaganda by the British). Opportunity fire models that capability without giving the British player a full turn of action out of sequence. The German player moves and the British player shoots at them as they move. Simple, historical, the British player stays engaged during the German turn and vice-versa.

DAMOS handles reactions differently. Non-phasing units within a Zone of Influence can attempt reaction movement when enemy units approach. The reacting player rolls against the unit's quality to see if the reaction succeeds. Better-trained formations react faster and more reliably. A Soviet rifle division in 1941 is unlikely to react in time. A German panzer division almost certainly will. The same mechanic applied to different quality ratings produces that asymmetry.

Great Northern War includes interception mechanics where forces can attempt to intercept enemy movement. In the LCOS series, units can intercept when enemies move into a EZOC. These are narrow responses to specific triggers, not full activations. The non-phasing player acts only in defined circumstances, which keeps the SOP predictable while adding meaningful interaction.

Kevin Zucker instilled in me a healthy skepticism of chrome, and that skepticism applies to reaction systems as much as anything else. A reaction mechanic should solve a specific problem. If your game has a passivity issue, reactions help. If your simulation needs to model a defender's ability to respond to threats, reactions help. But adding reactions because they seem like a good idea adds complexity to every single turn of the game. The non-phasing player now evaluates triggers after every move. The phasing player anticipates reactions when planning movement. If the reaction mechanic does not pay for its complexity with better gameplay or better simulation, cut it.

## Timing and Phase Order

The order in which phases occur within a turn is not arbitrary. It is a design decision with consequences for how the game plays.

Consider supply. If you check supply at the beginning of the turn before movement, units out of supply suffer penalties before the player has a chance to reconnect them. Supply disruption becomes more punishing. If you check supply at the end of the turn after movement, the player can maneuver to restore supply lines before the check occurs. Disruption becomes a temporary inconvenience. Neither approach is wrong, but they produce different games. The timing of the supply check determines how much weight supply carries as a strategic concern.

The same logic applies to recovery from disruption. If disrupted units recover at the start of their turn, disruption is a one-turn penalty. If they recover at the end of their turn, they spend a full turn impaired. If recovery requires skipping movement or combat, disruption becomes a serious operational cost. I included disruption in Imperial Bayonets and the timing of recovery was critical. French units hit by Krupp artillery fire needed to spend time recovering before they could act again. If recovery had been instant at the start of the turn, disruption would have been meaningless. The whole point was modeling the shock of breechloading artillery on troops that had never experienced it.

Zucker was skeptical I should include disruption in Imperial Bayonets at all. His argument was that the system should handle the effects of artillery holistically, that if the combat results and modifiers were designed right, you would not need a separate disruption state. I disagreed. Disruption was one of the easier lightweight ways to model the specific effect of French troops getting shattered by Krupp artillery at ranges they could not answer. The Chassepot outranged the needle gun, but it could not answer Krupp steel. A simple disruption status captured that without building a separate artillery subsystem. I still think I was right, but Zucker's instinct to question mechanical additions was sound. Every phase you add to the sequence of play is a phase that runs every single turn. If it does not carry its weight, remove it.

Reinforcement timing matters too. If reinforcements arrive at the start of the turn, they are available for the full turn's movement and combat. If they arrive at the end, they sit on the map but cannot act until next turn, giving the opponent a chance to react to their arrival. Reinforcements that arrived and threw themselves into the battle should appear at the start. Reinforcements that arrived in the rear and needed time to deploy could appear at the end, but I recommend sticking with one implementation.

Weather determination belongs at the start of the turn, before any other phase. Weather affects movement costs, combat modifiers, and sometimes supply. Players need to know the weather before they make decisions. Putting weather determination anywhere else creates situations where a player commits to a plan and then discovers the weather invalidates it, which is frustrating rather than interesting. Weather, reinforcements, supply: these are administrative phases. They handle the historical and logistical context of the turn. They are the infrastructure that makes the simulation work.

## The SOP as Design Output

Your sequence of play will emerge from the game you are building. You design a movement system, a combat system, a supply system, and the SOP is the structure that tells the player when to use each one. The SOP is an output of the design process, not something you decide in advance.

But timing matters, and the order you choose has downstream effects that are easy to miss. I have found it useful to write out the full sequence of play early in development, even before all the systems are finalized, and revisit it as the design evolves. Moving a phase from one position to another can change how the entire game feels. Swap the order of combat and movement, letting players fight first and then advance rather than moving into position and then fighting, and you have a different game. Both structures exist in published designs. The choice between them should be deliberate.

The test for whether your SOP is working is simple. Set up a game turn and walk through it. Does the sequence feel logical? Does each phase lead naturally into the next? Are there phases where nothing happens most turns? If a phase is irrelevant in most turns, consider making it conditional rather than mandatory. "Check supply if any unit is not in range of a supply source" is better than "Check supply for every unit every turn" if most units are always in supply.

## Administrative Phases vs. Chrome

There is a distinction worth drawing between administrative phases and chrome, because the line between them affects how you build your SOP.

Administrative phases handle the historical infrastructure of the conflict. Weather determination, reinforcement arrival, supply checks, victory point tallying. These are the framework within which tactical and operational decisions occur. An Eastern Front game without supply is not simulating the Eastern Front. A Napoleonic game without reinforcement schedules ignores the arrival of forces that shaped the battle's outcome. These phases belong in the SOP because the simulation requires them.

Chrome is mechanical granularity that adds detail without adding decisions. Morale recovery rolls for every unit every turn. Detailed ammunition tracking. Disruption states that exist because the designer thought they were interesting rather than because the simulation demanded them. Chrome has a place in wargame design. I have used it when it solves a specific problem, as disruption does in Imperial Bayonets. But every piece of chrome you add to the SOP runs every turn, and players feel the weight of it.

Ask about any phase in your SOP: does this phase produce a decision or a result that matters? If a weather roll changes movement costs and combat modifiers in ways that force the player to adapt their plan, the weather phase carries its weight. If a weather roll produces "clear" ninety percent of the time and the other ten percent changes nothing meaningful, the phase is dead weight. Cut it or make it matter.

## Building a Non-Linear SOP

Most wargame SOPs are linear. Phase 1 leads to Phase 2 leads to Phase 3. This is the default because it is the easiest structure to explain and execute. Non-linear SOPs exist, and they produce experiences that linear structures cannot.

Sedan 1940 is the most radical example in my own work. No fixed phase order within an activation. A formation's chit gets drawn and the activating player chooses what to do: move units, conduct fire, launch assaults, place units in overwatch, or any combination. The "sequence" is whatever the player decides based on the tactical situation. The 1940 campaign in France was characterized by commanders at every level making rapid decisions about what to prioritize in the moment. Guderian did not wait for a movement phase before ordering an assault. He saw an opportunity and acted. The non-linear SOP lets the player do the same.

The tradeoff is cognitive load. A linear SOP tells the player what to do next. A non-linear SOP asks them to decide what to do next. For Sedan 1940, that cognitive load is the game. The decisions about what to do with your activation are the most interesting choices the player makes. A non-linear SOP applied to a game where the interesting decisions live elsewhere, in combat planning or strategic resource allocation, would add complexity without adding fun.

## Writing It Down

The physical presentation of the SOP matters more than designers recognize. A player aid card with the complete sequence of play, formatted clearly, is essential for any game with more than a handful of phases. Players will reference it every turn for the first several games and periodically after that.

Write the SOP in clear, direct language. Be precise about what is mandatory and what is optional. "Move eligible units" tells the player this is the movement phase. "Units may be moved" tells them movement is optional, which matters if you do not want to force every unit to act. "Roll for weather" is better than "Weather is determined" because it tells the player who does what. The SOP is an instruction manual for running the simulation, and word choice in instructions carries mechanical weight. "Move all units" and "units may be moved" are different rules, not different phrasings of the same rule.

Number every phase and sub-phase. Use consistent formatting. If phases have conditional triggers, state the conditions explicitly. "If any unit is in an enemy ZOC at the start of this phase, resolve ZOC attrition" is clear. "ZOC attrition may occur" is not.

Every sequence of play is an algorithm that allows human beings to run the model you have designed. You are writing a program in natural language. The quality of that program determines whether players can execute your design or spend the evening flipping through the rulebook looking for clarification. The clearer and more well-designed the SOP, the easier time players will have running the game. Treat it with the same rigor you bring to your CRT or your movement system.

## Common SOP Patterns

![Sequence of play flowchart]({{ site.baseurl }}/assets/images/sop-flowchart.png)

To make this concrete, here are the structural patterns I see most often and have used in my own work.

**The Classic Wargame Turn:**
1. Weather/Administrative Phase
2. Reinforcement Phase
3. Supply Phase
4. Movement Phase
5. Combat Phase
6. Exploitation/Mechanized Movement Phase
7. End Phase (victory check, marker removal)

This is the SPI/AH standard. Thousands of games use some variant of it. The structure has survived because it maps onto how military operations unfold: logistics first, then maneuver, then combat, then exploitation of results.

**The Double-Impulse Turn:**
1. First Player Movement
2. First Player Combat
3. Second Player Movement
4. Second Player Combat

This is IGO-UGO with both players acting within the same turn. Many of my games use this structure. It keeps the simplicity of IGO-UGO while ensuring both sides act within each game turn rather than alternating full turns.

**The Chit-Pull Turn:**
1. Administrative Phase (weather, supply, reinforcements)
2. Activation Phase (draw chits until cup is empty; each activation allows movement and/or combat)
3. End Phase

This is the Sedan 1940 pattern. The administrative work happens once at the top, and then the game is pure activation until the turn ends. The simplicity of the outer structure compensates for the complexity of the non-linear activations within it.

**The Reaction-Enhanced IGO-UGO Turn:**
1. Phasing Player Movement (non-phasing player may conduct opportunity fire/reactions)
2. Phasing Player Combat
3. Non-Phasing Player Reaction Phase (limited movement and/or combat for reserve units)
4. Swap phasing player and repeat

This is close to what Mons 1914 and Verdun use. The reaction opportunities break the passivity of pure IGO-UGO without abandoning the structure entirely.

These are templates, not prescriptions. Your game's subject and your design goals will tell you which pattern to start with. Playtesting will tell you how to modify it.
