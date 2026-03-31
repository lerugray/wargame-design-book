---
title: "Formations, Facing, and Posture"
chapter_number: 8
nav_order: 8
layout: chapter
---


The previous chapter covered how units move across the map. This one covers how they orient themselves while doing it. Facing and formation mechanics control what a unit can see, where it can shoot, and how vulnerable it is to attack from different directions. These mechanics produce tactical decisions when they work and bookkeeping when they do not.

## When Facing Matters

Facing is a mechanic inherited from miniature wargaming, where physical models on a tabletop have a literal front and back. In hex-and-counter games, facing means the counter points toward a specific hexside or hexspine, and that orientation determines its front, flanks, and rear. Attacks against the flank or rear receive bonuses. Units project ZOC only into their front hexes. The unit can only move into the hexes it faces.

This matters most for pre-20th century tactical combat, where formations fought in lines and the direction a unit faced determined its combat effectiveness. A Napoleonic infantry battalion in line could deliver devastating fire to its front but could do nothing if cavalry hit its flank. A Greek phalanx was a wall of shields and spears from the front and a crowd of unarmored men from behind.

Facing loses its grip as warfare modernizes. By 1866, Prussian infantry were going prone and fighting from dispersed positions thanks to the needle gun. A prone skirmish line does not have a meaningful facing the way a Napoleonic line does. By the Second World War, infantry squads could reorient in seconds. ASL, one of the most detailed tactical wargames ever made, omits unit facing. The designers knew that at their scale, a squad's orientation changed too fast to be worth tracking turn by turn.

Ask whether the historical subject demands facing, not whether your game is tactical enough to justify it. If the conflict you are simulating featured formations whose orientation relative to the enemy was a decisive factor in combat outcomes, facing belongs in your game. If it did not, facing is overhead.

## Hexside vs. Hexspine Facing

When you include facing, units will point either toward a hexside or toward a hexspine. Both give six possible orientations. The choice affects how facing interacts with the hex grid.

Hexside facing means the unit points at one of the six edges of its hex. Hexspine facing means it points at one of the six vertices. Each option produces a different geometry for front, flank, and rear hexes, and each interacts with turning costs in its own way.

Hex orientation determines which option looks right. With pointy-top hexes, where a vertex points straight up and down, hexspine facing lets two opposing lines point at each other across the map. That looks like a battlefield. Hexside facing in the same grid has them staring past each other at hex edges, which looks wrong even when the mechanics work. Flat-top hexes flip the geometry: hexside facing produces the straight-across alignment and hexspine creates the offset.

I prefer hexspine facing with pointy-top hexes. Marathon uses this combination and opposing phalanx lines face each other without any angular awkwardness. The facing type and the hex orientation are a package deal. Pick the combination that makes your map look like the battle it represents. If it looks wrong on the map, players will feel it before they can articulate why.

## Formations

Formation mechanics model the difference between how a unit moves and how it fights. Units need one posture to cover ground and a different posture to engage the enemy. Moving in fighting formation is slow. Arriving near the enemy in marching formation is fatal. The cost of switching between these states is one of the most important design levers in a wargame.

At the tactical level, this means column versus line. A battalion in column can move along roads quickly but presents a concentrated target and cannot bring its full firepower to bear. A battalion in line can deliver devastating volleys but moves at a crawl and falls apart crossing rough terrain. The historical challenge for commanders was timing the transition. Deploy too early and you waste hours covering ground in line. Deploy too late and the enemy catches you in column.

At the grand-tactical level, formation can be abstracted into Deployed and Travel modes. The mechanical idea is the same. Travel mode gives higher movement and lower combat capability. Deployed mode does the reverse. At the scale of battalions and regiments, the specific formation matters less than whether the force is configured for movement or for fighting.

In Koniggratz and Mars La Tour, units have March Formation with 4 MP and Battle Formation with 1 MP. Enemy Zones of Influence force March Formation units to flip to Battle Formation and stop. The transition is not optional. You do not choose to deploy. The proximity of the enemy forces deployment on you.

Sedan 1940 uses the same concept of Travel Mode and Deployed Mode but handles the transition differently. The player decides when to switch. Travel Mode offers higher movement but imposes penalties when engaged. The risk is voluntary: you choose to stay in Travel Mode for the speed, knowing that contact with the enemy will punish you for it.

## Formation and Facing Together

Some systems tie formation state to facing orientation. In my game on Marathon, deployed units face a hexspine while units in march formation face a hexside. The formation a unit is in determines how it orients on the map, which determines its front, flank, and rear hexes.

I tried a more complex version of this in an early tactical variant of Imperial Bayonets. Units in column formation faced a hexside, which channeled their movement into the hexes ahead of them. Units in line formation faced a hexspine, sacrificing mobility for firepower across a wider front. On paper it looked elegant. In practice it was a nightmare. The constant tracking of which units faced which direction in which formation, combined with the cost of switching between states, produced a game that was more puzzle than simulation. Hermann Luttmann was kind enough to humor me by helping playtest it at a convention, but the game was not working. The formation-facing interaction created overhead without adding proportional decisions.

Combining facing and formation can work, but only when the interaction is clean enough that players internalize it rather than consult the rules every turn. Marathon's system works because the formation states are simple and the facing rules are short. The early Imperial Bayonets variant failed because the tactical scale magnified every interaction into a separate case to manage.

An early version of that same game included a scenario for Bazeilles, a battle from the Franco-Prussian War fought almost entirely from buildings. The scenario still had facing rules. French units garrisoned in houses had front and rear hexes. It made no sense. If your battle does not involve linear formations maneuvering in the open, facing is not adding anything, no matter how tactical the scale.

## The Cost of Changing Formation

Formation changes should cost something. The design decision is how much and what kind of cost.

The most common approach is spending movement points. In Marathon, a unit must spend its entire movement allowance to change formation. This is a steep cost that makes the decision consequential. You cannot march up to the enemy, deploy, and attack in the same activation. You march, then next turn you deploy, then you fight. The tempo of the approach is built into the formation change cost.

Other systems use partial MP costs. A unit might spend half its movement to change formation, allowing some residual movement afterward. This is more forgiving and works for games where the designer wants formation changes to be a consideration rather than a commitment.

Some games impose combat penalties instead of or in addition to MP costs. In Marathon, attacking a unit in march formation grants a +3 DRM to the attacker. The formation change costs your full movement allowance, but getting caught before you complete it is worse. Other systems allow opportunity fire when a unit changes formation within range of the enemy, punishing a force that reorganizes under observation.

Command systems can restrict formation changes, but be cautious about leaning too hard on this. The battalion commander or the unit's NCOs managed formation transitions. Higher command decided where the army went and when it attacked. Generals did not micromanage whether a battalion was in column or line. Unless your system models command dysfunction at the tactical level, formation changes should be a function of the unit's own capability and the situation on the ground, not something that requires orders from headquarters.

## Facing and ZOC

In systems with facing, ZOC projects only into a unit's front hexes. A unit does not project a zone of control into its flank or rear hexes. Flanking forces can move through those hexes without stopping.

One useful exception is skirmishers. Light troops historically operated in loose formations, moving and firing in any direction without maintaining a fixed front. In Marathon, skirmisher units treat all six adjacent hexes as front hexes. They project ZOC in every direction, can move and fire freely, and have no flank or rear to exploit. This matches how light troops operated compared to heavier line formations.

Flank and rear attacks receive bonuses in most systems that use facing. Marathon gives +1 DRM for attacks into an enemy's flank and +2 DRM for attacks into the rear. These modifiers are small enough that flanking is an advantage rather than an automatic kill, but large enough that players work hard to protect their flanks and exploit the enemy's.

Facing also affects retreat. A unit that must retreat will fall back through its rear hexes. If enemy units occupy or project ZOC into those hexes, the retreating unit may be eliminated. Encirclement emerges from the facing and ZOC rules working together, without requiring a separate encirclement mechanic.

## The Rightward Drift

Marathon includes an asymmetric turning cost for phalanx units. Turning to the right costs 1 MP. Turning to the left costs 2 MP. This models a phenomenon described by classical scholars: because each man in a hoplite phalanx drifted to the right, trying to stay behind his neighbor's shield, the entire formation had a natural tendency to slide rightward during movement.

I could have modeled this by forcing phalanx units to shift one hex to the right every other turn of movement. That would have been historically precise and mechanically miserable. The asymmetric turning cost captures the same idea. The phalanx turns more naturally to the right because the formation's structure favors it. Players feel the constraint without tracking lateral drift hex by hex.

The phenomenon is real and tactically significant. A direct simulation would produce accurate results and terrible gameplay. The abstracted version communicates the same constraint through movement point costs, a mechanism players already understand, and requires no additional rules.

## The Digital Advantage

Many facing and formation mechanics that are too fiddly for cardboard work well in digital implementations. The Wargame Design Studio series handles facing, formation changes, and their interactions with a level of detail that would be unbearable on a tabletop. The computer tracks orientation, calculates modifiers, and resolves formation changes. The player makes decisions. The software handles bookkeeping.

If you find yourself designing a facing or formation system that requires constant reference to charts and edge cases, ask whether you are designing a tabletop game or a computer game. The two media have different tolerances for mechanical complexity, and a system that shines in one can be unbearable in the other.

## Choosing What to Include

If you are designing a game and wondering whether to include facing, formations, or both, the decision follows from your scale and subject. Here is how I think about it.

**Tactical, ancient or medieval:** Facing and formations both. These conflicts were defined by the orientation and posture of the fighting unit. A hoplite phalanx, a Roman maniple, a medieval pike block. Facing determines who can fight and where. Formation determines whether the unit can move or hold. Marathon uses both, and the interaction between them is the game.

**Tactical, horse-and-musket era:** Facing and formations both, but watch the complexity. Napoleonic infantry had column, line, and square, each with distinct capabilities. The design temptation is to model all three plus transitions between them. That can work, but test whether the transitions produce decisions or just bookkeeping. If players spend more time managing formation changes than maneuvering, cut a formation state.

**Tactical, 20th century onward:** Formations rarely. Facing rarely. Modern infantry reorients in seconds. ASL omits facing for this reason. If your 20th century tactical game includes facing, you need a strong argument for why the constraint existed in your specific situation.

**Grand-tactical:** Formations yes, facing usually no. The distinction between march posture and combat posture is the core design lever at this scale. A brigade in travel mode versus deployed mode creates the right decisions. Facing a brigade counter at a hexspine does not, because the regiments within it are oriented in different directions depending on the tactical situation. Koniggratz, Mars La Tour, and Sedan 1940 all use formation states without facing at this scale.

**Operational and strategic:** Neither. Divisions and corps reorient continuously. Formation state and facing at these scales add management burden without producing decisions. If you need to model the difference between a force on the march and a force in defensive positions at operational scale, handle it through movement modes (strategic movement vs. normal movement) rather than formation counters.

## When to Leave It Out

Facing should not be included at the grand-tactical scale unless your game operates at a particularly small scale within that category. A brigade does not have a meaningful front and rear at five miles per hex. The individual regiments within it are oriented in various directions depending on the tactical situation, and the brigade's overall posture is better modeled through formation state than through a counter pointing at a hexspine.

At the operational and strategic level, facing is almost never appropriate. Divisions, corps, and armies orient and reorient continuously. Facing at these scales adds a management burden that produces no interesting decisions.

Even at the tactical level, facing is not automatic. If the conflict you are simulating involved forces that could reorient fast, such as modern infantry or guerrilla fighters, facing models a constraint that did not exist. Include it when the historical subject demands it.

## Case Study: Marathon and the Cost of Getting It Wrong

Marathon went through three versions of its facing and formation system before I found the one that worked.

The first version used hexside facing for all units. Phalanx lines faced each other at awkward angles on the map. Flanking attacks required counting hexsides and consulting a chart to determine whether the attacking hex qualified as flank or rear. Players stopped to argue about geometry. The facing rules were technically correct and produced miserable play.

The second version switched to hexspine facing, which solved the visual alignment problem. Opposing phalanx lines pointed straight at each other. But I kept a complex formation system with three states: march column, open order, and close order. Each state had different movement costs, different combat modifiers, and different facing rules. Changing between them required spending movement points and passing a command check. Playtesting revealed that players spent more time managing formation transitions than making tactical decisions. The three-state system modeled historical reality and buried it under procedure.

The third version, the one that shipped, uses hexspine facing with two formation states: march and deployed. March formation faces a hexside, deployed faces a hexspine. Changing formation costs your full movement allowance. Getting caught in march formation by the enemy gives the attacker a +3 DRM. The asymmetric turning cost (1 MP right, 2 MP left) captures the rightward drift of hoplite lines. The skirmisher exception (ZOC in all six hexes, no flank or rear) models light troops.

The system works because each rule produces a decision. Face the phalanx toward the enemy or angle it to protect a flank. Deploy now and fight next turn or gamble on one more turn of marching. Commit skirmishers to screen the approach or hold them back for flank protection. The rules are short enough that players internalize them after two turns and stop consulting the rulebook.

The lesson from the failed versions is that historical accuracy in formation mechanics does not guarantee good design. The three-state system was more historically precise than the two-state system. It was also worse. Precision that the player cannot act on is wasted complexity. The two-state system captures what mattered about ancient formation warfare: the tension between mobility and combat readiness, the vulnerability of units caught unprepared, and the physical constraints of maintaining a formation under pressure. It leaves out what did not produce decisions at the game's scale.

If your formation system needs a chart, it is too complex. If players manage it without thinking about it, you have found the right level of abstraction.
