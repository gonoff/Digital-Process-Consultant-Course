# L0.C1 Solutions Guide: Systems Analysis Project

## Navigation
**Course**: [[../../index|Course Home]] > [[../../Level0_index|Level 0]] > [[L0_C1_reading|Chapter 1]] > Solutions  
**Project**: [[L0_C1_project|View Project Assignment]]  
**Previous**: [[L0_C1_project|Project Assignment]]  
**Next**: [[L0_C2_reading|Chapter 2: Business Process Basics]]  
**Related**: [[L0_C1_reading|Chapter 1 Reading]] | [[L0_C1_quiz.html|Chapter 1 Quiz]]

---

## Purpose of This Guide

This solutions guide provides sample analyses and evaluation criteria to help instructors assess student work and help students understand the depth of analysis expected. It includes example solutions for different business scenarios and common mistake patterns.

## Sample Solution: Coffee Shop Wait Time Problem

### Sample Problem Statement

**Bean There Coffee** is a 25-seat independent coffee shop near a university campus that has been experiencing excessive customer wait times (averaging 8-12 minutes vs. industry standard of 3-5 minutes) for the past six months. This manifests as customers leaving the line before ordering, negative online reviews mentioning slow service, and visible frustration among both customers and staff during morning rush periods. 

The problem affects students who need quick service between classes, employees who face constant pressure and complaints, and the owner who has seen a 20% decline in repeat customers. Management has attempted to address this by hiring an additional part-time barista and installing a faster espresso machine, which reduced wait times slightly but increased labor costs by 30% while customer satisfaction scores remain low. The persistent nature of complaints across different times and staffing levels suggests systemic workflow issues rather than simple capacity problems.

*Analysis: This problem statement effectively identifies multiple symptoms, stakeholder impacts, attempted solutions, and hints at systemic causes. Word count: 148.*

### Sample Stakeholder Map

```
PRIMARY STAKEHOLDERS:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CUSTOMERS     │────│   EMPLOYEES     │────│      OWNER      │
│                 │    │                 │    │                 │
│ • Students      │    │ • Baristas      │    │ • Financial     │
│ • Professionals │    │ • Cashier       │    │   pressure      │
│ • Regulars      │    │ • Manager       │    │ • Reputation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         └──────────────│   SUPPLIERS     │──────────────┘
                        │                 │
                        │ • Coffee roaster│
                        │ • Food vendors  │
                        │ • Equipment     │
                        └─────────────────┘

SECONDARY STAKEHOLDERS:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   COMMUNITY     │    │  COMPETITORS    │    │   UNIVERSITY    │
│                 │    │                 │    │                 │
│ • Neighbors     │    │ • Chain stores  │    │ • Student body  │
│ • Local economy │    │ • Other cafes   │    │ • Faculty       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Sample Causal-Loop Diagram

```
    Customer Wait Time
           │ +
           ▼
    Customer Frustration ────────────(+)────────────► Negative Reviews
           │ +                                              │ +
           ▼                                                ▼
    Customer Abandonment                              Reputation Damage
           │ +                                              │ +
           ▼                                                ▼
    Revenue per Hour ◄────(-)────── Lost Customers ◄───────┘
           │ -                          ▲ +
           ▼                            │
    Owner Financial Pressure            │
           │ +                          │
           ▼                            │
    Pressure on Staff ──────────────────┘
           │ +
           ▼
    Employee Stress
           │ +
           ▼                    Employee Training Time
    Mistakes/Rework ◄────(-)──────────────────────────┐
           │ +                                        │ -
           ▼                                          │
    Service Time per Order                            │
           │ +                                        │
           ▼                                          │
    Customer Wait Time ──►(+)──► Staff Overtime ─────┘
                                       │ +
                                       ▼
                              Labor Costs ────►(+)──► Owner Financial Pressure

Legend:
+ = Same direction relationship
- = Opposite direction relationship
R1 = Reinforcing loop (Wait Time → Frustration → Abandonment → Pressure → Stress → Mistakes → Wait Time)
B1 = Balancing attempt (Pressure → Overtime → Higher costs → More pressure)
```

### Sample Intervention Analysis

**High-Leverage Point: Redesign Workflow Structure**
The highest leverage intervention would be restructuring the service workflow from a single-queue, sequential process to a parallel processing system with order staging. This addresses the root cause—process design—rather than just adding capacity. By separating order taking, payment, and fulfillment into parallel streams with visual tracking, customers would experience reduced wait times and increased transparency. This structural change would affect multiple system variables simultaneously: reducing employee stress, improving customer experience, and optimizing resource utilization.

**Medium-Leverage Point: Information Flow Improvement**
Implementing a simple order tracking system (numbered cups, digital display, or mobile notifications) would improve information flow between staff and customers. This reduces perceived wait time, decreases customer anxiety, and allows staff to manage expectations proactively. While not changing the fundamental process structure, it modifies system rules about information sharing and communication protocols.

**Low-Leverage Point: Staffing Level Adjustments**
Adding more staff during peak hours addresses capacity constraints but doesn't change underlying workflow inefficiencies. This parameter adjustment might reduce wait times temporarily but could create new problems: higher labor costs, coordination difficulties in limited space, and potential for diminishing returns as staff interfere with each other.

**Root Cause vs. Symptom Analysis**
The most obvious symptom-focused solution would be hiring more baristas or buying faster equipment—essentially throwing resources at the capacity problem. However, these approaches create policy resistance because they don't address workflow bottlenecks, role clarity, or process standardization. Adding staff to a poorly designed system can actually increase chaos and mistakes. Equipment upgrades might speed individual tasks but create new bottlenecks elsewhere in the process. These solutions also increase fixed costs, creating financial pressure that could lead to cost-cutting in other areas (training, quality ingredients), potentially making the underlying problems worse. Structural changes to workflow design are necessary because they address how work flows through the system, not just how much capacity exists at individual steps.

## Common Student Mistakes and Guidance

### Mistake 1: Linear Problem Definition
**Student writes:** "The coffee shop is slow because they don't have enough employees."

**Guidance:** This identifies a single cause-effect relationship without exploring system dynamics. Better approach: "Multiple factors interact to create wait times—workflow design, role definitions, customer arrival patterns, and staff coordination—creating feedback loops that perpetuate delays."

### Mistake 2: Superficial Stakeholder Analysis
**Student writes:** "Stakeholders are customers, employees, and owner."

**Guidance:** This misses the complexity of stakeholder relationships and sub-groups. Encourage students to think about: different customer segments with different needs, various employee roles with different perspectives, suppliers who might be affected by ordering patterns, and community impacts.

### Mistake 3: Fake Feedback Loops
**Student draws:** Customer complaints → Management fixes problem → Problem solved

**Guidance:** This isn't actually a feedback loop—it's a linear intervention. Real loops are circular: Customer complaints → Management pressure → Quick fixes → Unintended consequences → More problems → More complaints.

### Mistake 4: Single-Point Solutions
**Student proposes:** "Just hire more people during rush hour."

**Guidance:** This ignores system behavior and potential unintended consequences. Guide students to consider: How might adding people to a poorly designed system create new problems? What happens to labor costs? How does this affect service during off-peak hours?

## Evaluation Rubric

### Problem Statement Assessment

**Excellent (23-25 points):**
- Clearly identifies business context and multiple symptoms
- Quantifies impact where possible
- Mentions timeline and previous solution attempts
- Hints at systemic rather than isolated causes
- Stays within word limit while being comprehensive

**Proficient (20-22 points):**
- Identifies main problem and basic context
- Mentions some stakeholder impacts
- References some attempted solutions
- Shows awareness that problem is recurring
- Generally well-written and clear

**Developing (17-19 points):**
- Identifies basic problem but limited context
- Focuses mainly on symptoms without much depth
- Little mention of stakeholder impacts or attempted solutions
- Shows limited systems thinking perspective

**Inadequate (0-16 points):**
- Very brief or unclear problem description
- Focuses on single cause or blame assignment
- No evidence of systems thinking approach
- Poor writing quality or exceeds word limit significantly

### Causal-Loop Diagram Assessment

**Excellent (23-25 points):**
- Shows multiple complete feedback loops with proper notation
- Variables are meaningful and measurable
- Relationships are logical and realistic
- Includes both reinforcing and balancing dynamics
- Properly uses delay markers where appropriate
- Demonstrates sophisticated understanding of system behavior

**Proficient (20-22 points):**
- Shows at least one complete feedback loop
- Most relationships are logical
- Uses proper notation (arrows, +/- signs)
- Variables are relevant to the problem
- Shows good grasp of basic feedback concepts

**Developing (17-19 points):**
- Attempts to show feedback relationships but may have errors
- Some relationships unclear or illogical
- Basic notation present but may be incomplete
- Shows effort to understand system dynamics

**Inadequate (0-16 points):**
- No clear feedback loops identified
- Relationships are primarily linear
- Poor or missing notation
- Little evidence of systems thinking

### Intervention Analysis Assessment

**Excellent (23-25 points):**
- Clearly distinguishes between high, medium, and low leverage points
- Demonstrates understanding of why structural changes have higher leverage
- Sophisticated analysis of unintended consequences
- Shows awareness of policy resistance concepts
- Argues convincingly for root cause vs. symptom approaches

**Proficient (20-22 points):**
- Identifies some leverage differences between interventions
- Shows good understanding of system structure importance
- Recognizes some unintended consequences
- Makes reasonable arguments for structural approaches

**Developing (17-19 points):**
- Makes some attempt to differentiate intervention approaches
- Shows basic awareness of system vs. symptom solutions
- Limited analysis of leverage concepts
- Arguments are present but not well-developed

**Inadequate (0-16 points):**
- Interventions are primarily symptom-focused
- Little evidence of leverage point understanding
- No meaningful analysis of root causes
- Poor argumentation or very brief responses

## Additional Example Scenarios

### Scenario 2: Restaurant High Employee Turnover

**System Variables:** Employee satisfaction, training investment, service quality, customer tips, workload per person, hiring costs, management stress, scheduling difficulties

**Key Feedback Loops:**
- High turnover → increased workload for remaining staff → burnout → more turnover (reinforcing)
- Poor training → mistakes → customer complaints → management pressure → rushed hiring → poor training (reinforcing)
- High turnover → hiring costs → budget pressure → lower wages → difficulty attracting quality staff → high turnover (reinforcing)

**Leverage Points:**
- High: Change management paradigm about investment in employees
- Medium: Implement structured onboarding and mentorship systems
- Low: Increase wages without changing work environment

### Scenario 3: Retail Store Inventory Problems

**System Variables:** Stock levels, ordering frequency, storage space, cash flow, customer satisfaction, employee time, forecasting accuracy, supplier relationships

**Key Feedback Loops:**
- Stockouts → lost sales → cash flow problems → delayed ordering → more stockouts (reinforcing)
- Excess inventory → cash tied up → space constraints → rushed clearance → poor buying decisions → excess inventory (reinforcing)
- Poor forecasting → wrong orders → customer complaints → pressure for more inventory → higher carrying costs → budget pressure → less investment in forecasting (reinforcing)

## Teaching Tips

1. **Emphasize Observation:** Encourage students to spend time actually observing the business rather than making assumptions.

2. **Practice Loop Thinking:** Have students practice identifying feedback loops in simple, familiar systems before tackling complex business problems.

3. **Challenge Linear Solutions:** When students propose simple fixes, ask "What might be the unintended consequences of that approach?"

4. **Use Real Examples:** Share stories of well-intentioned business solutions that backfired due to systems effects.

5. **Encourage Multiple Perspectives:** Have students consider how different stakeholders might view the same problem differently.

This solutions guide provides a framework for both teaching and evaluating systems thinking applications in business contexts.

---

## Navigation
**Project Assignment**: [[L0_C1_project|Return to Project Assignment]]  
**Next Chapter**: [[L0_C2_reading|Chapter 2: Business Process Basics]]  
**Level Index**: [[../../Level0_index|Level 0 Index]]