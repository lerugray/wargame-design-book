---
title: "Combat Resolution"
chapter_number: 9
nav_order: 9
layout: chapter
---


Combat resolution is the mechanical heart of most wargames. Players maneuver their forces, position for advantage, commit to an attack, and then read the results off a table or resolve a procedure. The CRT determines whether a flanking maneuver pays off and whether a defensive position holds. The rest of the game's systems feed into this moment or flow from it. A combat system that produces historical results makes the whole game feel right. One that does not will undermine the best map, the best OOB, and the best sequence of play you can write.

This is also the part of design I find most creative. Building a CRT is an exercise in controlled probability. You are deciding what can happen, how often it should happen, and what it costs both sides. Few resources explain how to do this well. Richard Berg wrote a piece on the subject in SPI's Special Study #2 that remains one of the only serious treatments I know of. Part of the reason more does not exist is that there is no single correct method. The other reason is that designers who are good at it learned by studying other people's tables and iterating in spreadsheets until the results looked right.

## The Odds-Based CRT

The odds-based combat results table has been the standard approach since the early days of SPI and Avalon Hill. The mechanic is straightforward. Total the attacking strength points, total the defending strength points, and create a ratio. If 12 SP attack 4 SP, the ratio is 3:1. If 9 SP attack 6 SP, the ratio is 1.5:1, which most classic systems round down to 1:1 in favor of the defender. Some publishers round up at the half, including MMP's Standard Combat Series. Rostov '41, which I designed for SCS, uses this convention. Both approaches work. Rounding down is more traditional and gives the defender a slight edge in borderline situations. Rounding up is more forgiving to the attacker. It is a matter of preference. Find the column on the CRT that matches the ratio, roll a die, and cross-reference the result.

The system scales well. A 3:1 attack means the same thing whether you are pushing three divisions against one or thirty battalions against ten. The table does not distinguish between absolute numbers, only the relationship between forces. This makes odds-based tables suitable for scales from tactical firefights to strategic theater-level campaigns.

The columns on a typical CRT run from low odds on the left to high odds on the right. A 1:2 attack is desperate and will fail most of the time. A 3:1 attack is strong and will succeed most of the time. The results shift from bad for the attacker on the left to bad for the defender on the right. At low odds, the attacker risks elimination or retreat. At high odds, the defender faces the same. The middle columns produce uncertain outcomes where both sides might take losses.

If you want to understand how CRTs work, study the classics. SPI's The Marne, Soldiers, and Battle for Germany all have CRTs worth examining. Those tables will teach you more about combat resolution than reading about it in the abstract.

## Differential CRTs

The alternative to odds-based resolution is the differential table. Instead of creating a ratio, you subtract the defender's strength from the attacker's strength and use the resulting number as the column. If 10 SP attack 6 SP, the differential is +4. If 6 SP attack 10 SP, the differential is -4.

Differential tables eliminate the rounding that odds-based tables require, and they handle low-strength combat situations with more precision. Two units with 1 SP each fighting on an odds-based table produce results identical to two 20 SP stacks fighting at the same 1:1 ratio. On a differential table, the absolute size of the forces can matter, which some designers prefer.

The weakness is that differential tables can produce strange results at the extremes. The gap between +2 and +4 feels the same on the table, but the tactical situations producing those numbers can be different in ways the resolution does not capture. Hermann Luttmann uses differential tables in several of his designs and makes them work well. One trick I have borrowed from his approach is applying column shifts to the differential table based on traditional force ratios. If the attacker has a 3:1 advantage, shift the column right by two. You get the precision of a differential calculation with the intuitive scaling of odds-based ratios. Prigozhin's March of Justice uses this hybrid approach, and the table produces results that feel right across a wide range of combat situations.

I use differential tables in some of my more strategic games and sometimes in the context of tactical assaults within a larger operational system. For most designs, I prefer odds-based resolution for its simplicity and the half century of proven track record behind it.

## Dice Resolution

The die you choose shapes what your combat system can do. A single d6 gives flat probability. Each number from 1 to 6 has the same chance of appearing. A 2d6 roll produces a bell curve where 7 is the most common result and 2 or 12 are rare. This is not a cosmetic distinction. It changes how players experience combat and how you as the designer can tune outcomes.

Flat dice produce volatile results. On a 1d6, the chance of rolling a 1 is the same as rolling a 6. Extreme results show up often enough that players cannot rely on favorable odds to guarantee outcomes. I prefer 1d6 or 1d10 for games where I want combat to feel unpredictable. A Napoleonic battle where a 3:1 attack can still collapse captures something true about warfare. Commanders plan, commit forces, and sometimes the plan falls apart on contact.

A bell curve gives you finer control over outcomes. On 2d6, rolling a 7 happens about 17% of the time, but rolling a 2 happens less than 3% of the time. Middle results dominate. Small modifiers produce larger effects near the center of the curve because each +1 or -1 shifts a bigger slice of probability than it would on flat dice. I use bell curves in games where I want player agency to carry more weight than randomness. If you build a good plan and achieve a favorable ratio, a 2d6 table pays that off more consistently.

ASL uses 2d6 for all resolution, which fits a game that functions more as a competitive tactical exercise than a strict simulation. Skillful play produces consistent results on a bell curve. There is no wrong answer. Use flat dice when you want chaos and consequence. Use bell curves when you want the better plan to win more often.

## Combat Results

The results on your CRT determine what combat does to the units involved. The most common result types are step losses, retreats, exchanges, and eliminations. Each simulates something different, and the mix you choose sets the tone for the game.

**Step losses** reduce a unit's combat effectiveness. In many games, flipping a counter to its reduced side represents this. A step loss does not mean casualties in the literal sense. It represents the degradation of a formation's ability to fight: fatigue, disorganization, loss of key leaders, ammunition expenditure. Combat efficiency breaks down before a unit is destroyed. Using step losses as your primary result produces attritional games where forces wear down over time.

**Retreats** move the losing unit backward without destroying it. This is often the most common result at lower odds ratios. A 1:1 attack that produces a defender retreat is a success for the attacker without being catastrophic for the defender. In my World Undone series covering the opening campaigns of 1914, eliminations and reductions are rare. Forces rubberband back and forth as a result of battles, which matches what happened in those campaigns. The massive armies of 1914 fought, fell back, regrouped, and fought again. They did not annihilate each other in single engagements.

**Exchanges** require both sides to take losses. One common version eliminates the defender and requires the attacker to lose strength points equal to half the defender's total. Another version gives each side a single step loss. I use exchanges to introduce variance into CRTs so the results do not map too neatly along expected parameters. An exchange at 3:1 odds makes the attacker pay for a victory they expected to win clean. Players cannot treat high-odds attacks as automatic and free when exchanges appear in those columns.

**Eliminations** remove a unit from the game. These should be rare at most scales and in most conflicts. The threat of elimination gives teeth to the combat system, but if most fights can destroy a unit, the game becomes a knife fight where one bad roll ends a player's position. Calibrate how bloody your CRT is by looking at historical casualty rates for the conflict you are simulating. If the battle you are modeling produced 10% casualties, your CRT should not be eliminating a quarter of the forces engaged per turn.

Scale matters for result magnitudes. A defender retreating three hexes makes sense at tactical scale where each hex is a few hundred meters. At strategic scale where hexes are fifty miles across, a three-hex retreat represents an army falling back 150 miles from one engagement. Match your result types and magnitudes to your hex and turn scale.

## Column Shifts and Die Roll Modifiers

Column shifts and DRMs both adjust combat outcomes, but they work at different scales of effect and serve different design purposes.

A column shift moves the attack to a different odds column on the CRT. A one-column right shift turns a 2:1 into a 3:1. This changes the entire probability distribution, not a single number on the die. Column shifts should represent major tactical realities. Mountain terrain granting a two-column left shift in the defender's favor should feel significant when it applies. I keep column shifts scoped tight in my designs. Granting two shifts is acceptable for significant terrain like mountains or fortified cities, but stacking three or four shifts starts to undermine the odds calculation that the CRT is built on.

DRMs add or subtract from the die roll. A +1 DRM shifts the result one row on the table. This is a finer adjustment than a column shift and suits situations where the modifier represents an advantage without transforming the tactical picture. Combined arms bonuses, leader effects, flanking attacks, disruption penalties: these work well as DRMs. They add granularity to the combat system without the sledgehammer effect of changing the odds column.

Terrain and weather benefit the defender in most conflicts across most eras. A unit dug in on a ridge or defending a fortified city should be harder to dislodge, and your modifiers should reflect that. Positioning, combined arms, and concentration of force benefit the attacker. These are the tools an attacking player uses to create favorable odds, and the modifier system should reward good use of them.

The interaction between column shifts and DRMs gives your combat system its tactical texture. A player who maneuvers a flanking force into position to earn a +1 DRM while avoiding an attack across a river that would cost -1 DRM is making the kind of decision your game should reward.

## Artillery and Support Fire

How you handle artillery depends on scale. At tactical and grand-tactical scales, artillery units often appear as separate counters with their own combat mechanics. Bombardment tables and fire missions are distinct systems because at that scale, how a commander uses their guns is a separate decision from how they commit their infantry.

At operational and strategic scales, a division's combat strength includes its organic artillery. Separate artillery mechanics at these scales add complexity without adding decisions that matter at the level of abstraction you are working at. Exceptions exist. If a particular conflict featured artillery as a decisive independent arm, as heavy artillery was at Verdun, a separate system may be warranted.

Some games split the difference. Imperial Bayonets includes bombardment as a separate phase before combat, allowing artillery to disrupt defenders or create obligations that shape the main combat phase. PCS incorporates air support as a modifier within the overall combat system rather than a standalone resolution. The question you should ask is whether artillery use represents a separate decision in the conflict you are simulating, or whether it was one component of an integrated assault.

## Making Combat Match the Conflict

A Napoleonic battle should not feel like a World War I battle, and neither should feel like a modern armored engagement. The CRT is your primary tool for creating that distinction.

Napoleonic combat produced modest casualties in most engagements but generated catastrophic results when a formation broke. A CRT for a Napoleonic game should have retreat results dominating the middle columns with step losses appearing at extreme odds and devastating exchanges scattered through the table. Battles hinged on whether a formation held or ran, not on the physical destruction of the force.

World War I combat on the Western Front was attritional. Attacks produced casualties on both sides regardless of who held the ground at the end. A CRT for the Western Front should feature mutual losses as common results, with defender retreats being rare and hard-won. The attacker should expect to pay for each hex gained.

Modern maneuver warfare produces rapid, decisive results when one side achieves tactical surprise or technological superiority, but bogs down into attritional fighting when forces are matched. A CRT for a modern conflict might use high variance: devastating results at favorable odds, stalemates at parity.

Research is the only way to know how a particular conflict should feel. You cannot design a CRT for a war you have not studied. The casualty data and the campaign narratives tell you what combat looked like, and your table needs to reflect that.

## Diceless Combat

Not all combat resolution uses dice. Chit pull and card-based systems produce different kinds of uncertainty.

In a chit pull combat system, the randomness comes from drawing a value from a cup rather than rolling a die. PCS uses this approach. Each unit draws a combat chit at the moment of engagement, and the drawn value represents the unit's performance in that fight. A good unit can draw a low chit and a mediocre unit can draw a high one. The randomness lives inside the unit's capability rather than in an external die roll applied to the resolution.

Card-based combat, as used in games like Up Front and Combat Commander, resolves combat through card draws or card play. The deck functions as both randomizer and resource, because the cards you spend on combat are cards you cannot spend on other actions. This built-in tension between spending and saving does not exist in dice-based systems.

These are different tools for different design goals. Diceless combat tends to produce games where the resolution mechanic is more integrated with the rest of the game's systems, and where uncertainty distributes across the game in ways that dice cannot replicate.

## Designing Your First CRT

Your first CRT should be inspired by one you like. Find a published game with a combat system that appeals to you and use its CRT as a starting point. This is how designers in this hobby have learned for decades. Eighty percent of wargame design is building on the work of those who came before you, and the CRT is no exception.

My process is simple. I open a spreadsheet, write out the odds ratios as columns, and start filling in results. I iterate through different combinations until the table looks right to me. There is no formula. I am asking myself questions as I work: what should happen at 1:1? How bad should a 1:2 attack be? At what ratio does the defender start getting destroyed? How often should exchanges appear? I fill in results, look at the overall pattern, adjust, and repeat.

Start simple. A basic odds-based CRT with retreat and step loss results is enough. You can add column shifts for terrain later, DRMs for modifiers later, exchanges and special results later. Get the basic shape right first. Does a 3:1 attack succeed most of the time? Does a 1:1 attack feel like a coin flip? Does a 1:3 attack feel desperate? If the answers feel right, your CRT is working.

To make this concrete, here is a simple 1d6 CRT for a hypothetical operational game. Seven columns, five result types.

![Sedan 1940 national combat matrix example]({{ site.baseurl }}/assets/images/sedan-combat-matrix.png)

| 1d6 | 1:2 | 1:1 | 2:1 | 3:1 | 4:1 | 5:1 | 6:1 |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 1 | AE | AR2 | AR1 | EX | DR1 | DR1 | DR2 |
| 2 | AR2 | AR1 | EX | DR1 | DR1 | DR2 | DR2 |
| 3 | AR1 | EX | DR1 | DR1 | DR2 | DR2 | DE |
| 4 | AR1 | DR1 | DR1 | DR2 | DR2 | DE | DE |
| 5 | EX | DR1 | DR2 | DR2 | DE | DE | DE |
| 6 | DR1 | DR2 | DE | DE | DE | DE | DE |

AE = Attacker Eliminated. AR = Attacker Retreat (number of hexes). EX = Exchange (defender eliminated, attacker loses half the defender's SP). DR = Defender Retreat. DE = Defender Eliminated.

Three design decisions in this table worth examining. First, exchanges appear in the lower odds columns (1:2 through 2:1) but not the higher ones. At 1:2, the exchange sits on a roll of 5, meaning the attacker can still hurt the defender even at bad odds, but they pay for it. At 3:1, the exchange sits on a roll of 1, the worst result for a strong attack. Above 3:1, exchanges disappear because an attacker who has assembled overwhelming force should not be bleeding for it. Where you place exchanges determines how punishing combat feels at each odds level.

Second, the 1:1 column has no Attacker Eliminated result. A 1:1 attack is risky (you can retreat two hexes on a roll of 1) but it will not destroy your force. In many operational campaigns, commanders accepted 1:1 attacks when positioning demanded it. If 1:1 carried an elimination risk, players would never attack without a 2:1 advantage, and the game would stall. Removing AE from the 1:1 column encourages players to commit to borderline attacks, which produces more dynamic play.

Third, look at the high-odds columns. At 5:1 and 6:1, Defender Eliminated shows up on rolls of 4, 5, and 6 (or 3 through 6 at 6:1). A player who masses enough force to achieve 6:1 should expect to destroy the defender most of the time. If the high-odds columns are too gentle, there is no incentive to concentrate force. If they are too harsh, small units become disposable and players stop caring about individual formations. The balance between those extremes is where your game's personality lives.

This table is a starting point. Playtesting will tell you whether the 3:1 column is too bloody, whether retreats are too common at 1:1, whether the high-odds columns feel decisive enough. Adjust column by column until the results match the conflict you are simulating.

Expect the CRT to change more than any other component during development. Playtests will reveal problems your spreadsheet cannot. Results that seemed reasonable on paper will produce strange outcomes on the map. Adjust, playtest again, adjust again.

Once you are comfortable with established systems and understand what makes them work, begin to experiment. Introduce mechanics from games you admire. Combine approaches. Try a differential table with ratio column shifts. Try a dice pool system. The proven systems exist because they work, but the best games in this hobby have come from designers who understood the conventions well enough to deviate from them with purpose.

## Case Study: The Procedural Combat Series

PCS uses a combat system that shares little with my other designs. There is no printed CRT. Combat is differential-based, resolved through a procedural sequence rather than a single table lookup.

The core philosophy is unit quality over quantity. Combat interactions come down to one lead unit engaging one target defending unit. Adjacent friendly units provide support bonuses, but the fight itself is between two formations. This reflects how modern combat works at the operational level, where an engagement is dominated by the units in contact and supported by those nearby, rather than a mass of forces attacking at once.

Each unit draws a random combat chit at the moment of engagement. The chit value, combined with combat support adjustments from adjacent units, terrain, air support, and movement points spent approaching the target, produces a final combat strength for each side. Both sides then roll a d8 and add it to their combat strength. The difference between the two totals is the combat differential, which the players use to determine losses through a loss ratio.

The random chit draw gives PCS its identity. A unit's combat strength is not a fixed number printed on the counter. It varies from engagement to engagement. A player can commit forces to an attack and not know how effective they will be until the chit comes out of the cup. This models the fog and friction of modern combat, where the outcome of an engagement depends on factors no commander can predict or control.

Unit Quality Ratings differentiate between elite, regular, and poor formations. A higher-quality unit receives bonuses to its combat support adjustments. Quality matters more than mass in PCS, which matches how modern combined-arms warfare works in practice. A well-trained brigade with air support and favorable terrain can defeat a larger but less capable force.

I designed this system because traditional CRTs handle modern subjects poorly. An odds-based table treats combat as a contest of mass, which fits conflicts where massing force at the point of contact was the primary tactical challenge. Modern combat rewards positioning, quality, and combined arms integration. PCS makes those factors the core inputs to resolution rather than secondary modifiers on a ratio-based table.
