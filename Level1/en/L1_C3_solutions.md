# L1.C3 Solutions Guide: Root Cause Analysis Project

## Navigation
**Course**: [[../../index|Course Home]] > [[../../Level1_index|Level 1]] > [[L1_C3_reading|Chapter 3]] > Solutions  
**Project**: [[L1_C3_project|View Project Assignment]]  
**Previous**: [[L1_C3_project|Project Assignment]]  
**Next**: [[L1_C4_reading|Chapter 4: TO-BE Process Design and KPI Framework]]  
**Related**: [[L1_C3_reading|Chapter 3 Reading]] | [[L1_C3_quiz.html|Chapter 3 Quiz]]

---

## Purpose of This Guide

This solutions guide provides sample root cause analysis, evaluation frameworks, and common challenge patterns to help instructors assess student work and help students understand professional-level systematic problem-solving and business case development standards.

## Sample Solution: Customer Service Email Response Delays

### Sample Problem Definition and Impact Analysis

**Problem Statement:**
TechSupport Inc., a 75-person software company, experiences email customer support response delays averaging 18.5 hours, exceeding promised 4-hour response time by 360%. Current performance shows high variation (σ = 14.2 hours) with 68% of tickets violating SLA commitments. Problem scope includes initial customer email receipt through first substantive agent response, excluding automated acknowledgments. Issue has worsened 40% over past 6 months coinciding with 25% customer growth, indicating system capacity rather than temporary problem.

**Current State Impact Analysis:**
Direct costs include 12 hours weekly of senior manager time managing escalated complaints ($780/week labor cost), 8% customer churn rate directly attributed to support delays ($47,000 monthly revenue impact), and 15% support agent overtime costs due to firefighting mode ($3,200 monthly). Indirect costs encompass reduced customer satisfaction scores (3.1/5.0, down from 4.2), negative online reviews mentioning support delays (23% of recent reviews), and sales team spending 18% of time addressing support concerns instead of new business development. Total quantified annual impact: $645,000.

**Business Case Context:**
Company targeting 50% growth in next 18 months requires excellent customer support for retention and referrals. Current support delays create competitive disadvantage as customers frequently mention switching to competitors with faster response. Regulatory compliance requires documented response times for enterprise customers. Inaction cost escalates as customer base grows—each month delay in resolution increases annual impact by estimated $54,000. Support team morale declining due to constant firefighting, creating recruitment and retention challenges in tight labor market.

### Sample Systematic Root Cause Analysis

**5 Whys Analysis:**

**Problem**: Customer support email responses average 18.5 hours

**Why #1**: Why do email responses take 18.5 hours on average?
*Because tickets accumulate in queues waiting for agent attention while agents work on complex issues*

**Why #2**: Why do tickets accumulate while agents work complex issues?
*Because there's no ticket prioritization system, so agents tackle emails chronologically regardless of complexity or urgency*

**Why #3**: Why is there no prioritization system?
*Because the current helpdesk software doesn't support priority routing, and management thought chronological was "fairest" to customers*

**Why #4**: Why doesn't the helpdesk software support priority routing?
*Because the company chose the lowest-cost solution 3 years ago without considering workflow features, focusing only on basic ticket tracking*

**Why #5**: Why was the purchasing decision made without considering workflow features?
*Because IT budget was tight and no one analyzed the cost of poor support workflow versus software feature investment*

**Root Cause**: Technology investment decisions that prioritized upfront cost savings over operational efficiency, resulting in inadequate workflow capabilities that create systemic delays.

**Fishbone Diagram Analysis:**

**People Causes:**
- Agent experience variation: New agents average 28 hours response time vs. 12 hours for experienced agents
- No specialized expertise routing: Complex technical issues handled by any available agent regardless of skills
- Training gaps in efficiency techniques: Agents lack templates, shortcuts, and escalation procedures
- Manager availability for complex escalations: Only 1 supervisor for 8 agents, creating approval bottlenecks

**Process Causes:**
- Chronological email handling regardless of complexity or priority
- No standard response templates for common issues (60% of tickets are routine)
- Multiple handoffs for technical issues requiring developer input
- Customer information scattered across 3 systems requiring time-consuming lookups

**Technology Causes:**
- Helpdesk software lacks priority classification, automated routing, or workload balancing
- No integration between helpdesk and customer database, forcing manual account lookups
- Email threading issues causing agents to miss previous correspondence
- No real-time visibility into team workload or individual agent capacity

**Environment Causes:**
- Open office layout with constant interruptions breaking concentration
- Peak hour demand (9 AM-12 PM) exceeds capacity by 200% with no overflow procedures
- Customer expectations set by marketing promises without operational input
- No performance dashboards creating lack of awareness about delay patterns

**Materials Causes:**
- Knowledge base outdated with 35% of articles more than 12 months old
- Product documentation incomplete for recent feature releases
- Customer account information incomplete, requiring time-consuming verification
- No decision trees or troubleshooting guides for common issues

**Data-Driven Cause Validation:**

**Priority Analysis (Pareto):**
- Lack of ticket prioritization: 42% of total delay time
- Agent skill/experience mismatch: 28% of total delay time
- System integration inefficiencies: 18% of total delay time
- Knowledge base inadequacy: 12% of total delay time

**Statistical Evidence:**
- Correlation between ticket complexity and response time: r = 0.73 (strong)
- Agent experience vs. efficiency: New agents (<6 months) average 2.3x longer than experienced
- Time-of-day pattern: 73% of delays occur during 9 AM-12 PM peak period
- Response time by ticket type: Technical issues 26.3 hrs avg, Billing issues 8.7 hrs avg, General questions 4.2 hrs avg

### Sample Data Collection Strategy

**Data Requirements Analysis:**
Baseline measurements need: Individual ticket response times by agent, complexity, and type; agent utilization and capacity data; customer satisfaction correlation with response times; system performance metrics showing lookup times and integration delays. Quality requirements include real-time timestamp accuracy (±1 minute), 100% ticket coverage for statistical reliability, customer feedback correlation within 24 hours of ticket resolution. Collection period minimum 8 weeks to capture seasonal patterns and agent learning curves.

**Multi-Source Collection Plan:**

**System Data Collection:**
- Helpdesk database: Export all ticket timestamps, agent assignments, resolution times, and customer satisfaction scores for 12-week period (n≈2,400 tickets)
- Email server logs: Response time data validation and email threading analysis
- Customer database: Account lookup frequency and duration measurement via system monitoring
- Performance monitoring: System response times during peak vs. off-peak periods

**Observational Data Collection:**
- Time studies: Shadow 6 agents for 4-hour sessions documenting workflow steps and interruptions
- Agent screen recording (with permission): Capture 20 ticket resolution sessions across complexity levels
- Customer interaction observation: Monitor 15 phone escalations to understand email failure patterns
- Knowledge base usage tracking: Document search patterns and success rates for information retrieval

**Survey Data Collection:**
- Agent experience survey: 15-question instrument covering workflow efficiency, system usability, training needs (target: 100% response rate, n=8)
- Customer satisfaction follow-up: 5-question survey sent 48 hours after ticket resolution asking specifically about response time expectations
- Manager perspective survey: Supervisor insights on capacity planning, escalation patterns, and improvement priorities

**Interview Data Collection:**
- Structured interviews with all 8 agents (30 minutes each): Workflow pain points, informal procedures, improvement suggestions
- Customer focus group: 6 customers who experienced delays, understanding impact and expectations
- IT system administrator interview: Technical constraints, integration possibilities, upgrade options

**Statistical Rigor and Sampling:**
Sample size calculation indicates minimum 385 tickets needed for 95% confidence, ±5% margin of error. Stratified sampling ensures representation across: Agent experience levels (new <6mo, experienced 6-24mo, senior >24mo), ticket complexity (low, medium, high), time periods (peak 9-12 AM, normal 12-5 PM, evening 5-8 PM), customer types (free, paid, enterprise). Control for seasonal effects by including holiday periods and month-end billing cycles.

### Sample Business Case Development

**Current State Cost Analysis:**

**Direct Costs (Annual):**
- Management escalation time: 12 hrs/week × $65/hour × 52 weeks = $40,560
- Agent overtime due to firefighting: $3,200/month × 12 = $38,400
- Customer churn from support delays: 8% × $564,000 annual customer value = $45,120
- Negative review impact on new sales: Estimated 15% of prospects cite reviews, 23% mention support delays = $89,000 lost revenue

**Indirect Costs (Annual):**
- Sales team time on support issues: 18% × 4 salespeople × $75,000 salary = $54,000
- Reduced customer lifetime value from satisfaction drop: 1.1 point decrease × 400 customers × $235 impact = $94,000
- Agent recruitment/training from turnover: 2 additional departures × $15,000 replacement cost = $30,000
- Opportunity cost of delayed customer expansion: Poor support delays upsells by average 3.2 months × $28,000 monthly expansion revenue = $358,400

**Total Annual Impact: $749,480**

**Solution Investment Analysis:**

**Implementation Costs:**
- Helpdesk software upgrade with priority routing: $18,000 annually ($45,000 3-year)
- System integration project (helpdesk ↔ customer database): $35,000 one-time
- Agent training on new procedures and templates: $12,000 one-time
- Knowledge base overhaul and template development: $8,000 one-time
- Project management and change management: $15,000 one-time

**Total 3-Year Investment: $115,000**

**Return on Investment Calculation:**

**Expected Benefits (Annual):**
- Response time improvement (18.5 hrs → 4 hrs target): 75% reduction in escalation management = $30,420 savings
- Customer churn reduction (8% → 3%): 5% churn improvement × $564,000 = $28,200 revenue retention
- Agent efficiency improvement: 25% productivity gain = $96,000 equivalent capacity increase
- Sales team refocus on selling: Recovery of 18% time = $54,000 value
- Customer satisfaction improvement driving expansion: 2.5 month acceleration = $179,000 annual value

**Total Annual Benefits: $387,620**

**ROI Analysis:**
- Payback period: 3.6 months
- 3-year NPV (10% discount): $853,000
- 3-year ROI: 642%
- Break-even point: Month 4 of implementation

### Sample Implementation Recommendations

**Phase 1 (0-3 months): Quick Wins**
Implement ticket prioritization procedures manually while new software is configured, develop response templates for 15 most common ticket types (covering 60% of volume), create agent specialization for technical vs. billing issues, establish manager escalation protocols for complex issues. Expected 30% response time improvement with minimal cost.

**Phase 2 (3-12 months): Systematic Improvements**
Deploy new helpdesk software with automated priority routing, complete system integration eliminating manual lookups, implement comprehensive agent training program, overhaul knowledge base with searchable troubleshooting guides. Expected additional 40% improvement reaching 4-hour average target.

**Phase 3 (1-2 years): Strategic Enhancements**
Implement customer self-service portal reducing simple ticket volume by 35%, develop AI-assisted response suggestions, create predictive analytics for capacity planning, establish customer success program preventing issues before they require support. Target: 2-hour average response time with improved customer satisfaction.

## Evaluation Framework

### Problem Definition Assessment (25 points)

**Outstanding (22-25 points):**
- Clear, specific problem statement with quantified performance gaps
- Comprehensive impact analysis including direct, indirect, and opportunity costs
- Strong business context explaining strategic importance and urgency
- Well-defined scope with clear boundaries and stakeholder identification

**Proficient (18-21 points):**
- Good problem definition with adequate quantification
- Reasonable impact analysis covering major cost categories
- Basic business context and priority justification
- Clear scope definition with minor boundary ambiguities

**Developing (15-17 points):**
- Basic problem statement with limited quantification
- Simple impact analysis missing some cost categories
- Limited business context or priority justification
- Unclear scope boundaries or stakeholder identification

**Inadequate (0-14 points):**
- Vague problem statement without quantification
- Missing or inadequate impact analysis
- No business context or priority justification
- Poorly defined scope or missing stakeholder consideration

### Root Cause Analysis Quality (30 points)

**Outstanding (27-30 points):**
- Systematic 5 Whys analysis with evidence supporting each level
- Comprehensive fishbone analysis examining all relevant cause categories
- Strong data validation distinguishing root causes from symptoms
- Clear prioritization of causes by impact and feasibility

**Proficient (22-26 points):**
- Good 5 Whys analysis with reasonable evidence
- Adequate fishbone analysis covering major cause categories
- Basic data validation with some statistical support
- Reasonable cause prioritization with general justification

**Developing (18-21 points):**
- Basic 5 Whys analysis with limited evidence
- Simple fishbone analysis missing some categories
- Limited data validation without statistical rigor
- Simple cause identification without prioritization

**Inadequate (0-17 points):**
- Poor or incomplete 5 Whys analysis
- Missing or inadequate fishbone analysis
- No data validation or statistical support
- Failure to distinguish causes from symptoms

### Data Collection Strategy (25 points)

**Outstanding (22-25 points):**
- Comprehensive strategy with multiple data sources and collection methods
- Appropriate statistical sampling methodology with sample size calculations
- Clear data quality requirements and validation procedures
- Realistic timeline and resource requirements

**Proficient (18-21 points):**
- Good strategy covering major data needs with multiple sources
- Basic sampling methodology with adequate statistical considerations
- General data quality considerations and collection procedures
- Reasonable timeline and resource planning

**Developing (15-17 points):**
- Basic strategy with limited data sources or collection methods
- Simple sampling approach without statistical rigor
- Minimal data quality considerations
- Limited timeline or resource planning

**Inadequate (0-14 points):**
- Poor or missing data collection strategy
- No statistical sampling considerations
- Missing data quality requirements
- Unrealistic or missing implementation planning

### Business Case Development (20 points)

**Outstanding (18-20 points):**
- Comprehensive cost analysis including direct, indirect, and opportunity costs
- Realistic investment estimates with detailed breakdown
- Compelling ROI analysis with sensitivity analysis and risk assessment
- Clear financial justification with multiple scenarios

**Proficient (15-17 points):**
- Good cost analysis covering major cost categories
- Reasonable investment estimates with basic breakdown
- Adequate ROI analysis with basic financial justification
- General risk considerations without detailed analysis

**Developing (12-14 points):**
- Basic cost analysis with limited categories
- Simple investment estimates without detailed breakdown
- Limited ROI analysis with minimal financial justification
- Little to no risk consideration

**Inadequate (0-11 points):**
- Poor or missing cost analysis
- Unrealistic or missing investment estimates
- No meaningful ROI analysis or financial justification
- No risk consideration or sensitivity analysis

## Common Student Mistakes and Guidance

### Mistake 1: Confusing Symptoms with Root Causes
**Student approach:** Identifies "employees are slow" as root cause
**Guidance:** Push deeper—why are employees slow? What systemic issues create this symptom? Use data to validate each level of analysis.

### Mistake 2: Stopping at Convenient Explanations
**Student approach:** Blames "insufficient training" without investigating why training is insufficient
**Guidance:** Each "why" should reveal deeper systemic issues. Don't stop at explanations that blame individuals rather than systems.

### Mistake 3: Inadequate Data Collection Planning
**Student approach:** Plans to "survey some people" without sampling methodology
**Guidance:** Specify sample sizes, sampling methods, bias controls, and statistical analysis approaches for reliable conclusions.

### Mistake 4: Unrealistic Business Case Assumptions
**Student approach:** Assumes 90% problem elimination with minimal investment
**Guidance:** Use conservative benefit estimates, realistic implementation costs, and include risk factors. Validate assumptions with stakeholder input.

### Mistake 5: Generic Implementation Recommendations
**Student approach:** Suggests "provide more training" without specifics
**Guidance:** Recommendations must address identified root causes with specific actions, timelines, resources, and success metrics.

### Mistake 6: Poor Statistical Analysis
**Student approach:** Claims correlations without statistical testing
**Guidance:** Use appropriate statistical tools (control charts, correlation analysis, Pareto analysis) with proper interpretation and significance testing.

## Teaching Tips

1. **Emphasize Evidence-Based Analysis:** Require students to support each level of root cause analysis with data or stakeholder validation. Discourage speculation.

2. **Teach Statistical Thinking:** Help students understand when to use different statistical tools and how to interpret results correctly. Practice with real datasets.

3. **Connect to Business Reality:** Emphasize that business cases must be realistic and conservative. Share examples of failed projects due to overly optimistic assumptions.

4. **Focus on Implementation:** Root cause analysis is worthless without actionable solutions. Teach students to think like implementers, not just analysts.

5. **Validate with Stakeholders:** Encourage students to test their conclusions with people who experience the problem. Often reveals gaps in analysis.

6. **Practice with Complex Problems:** Simple problems don't require sophisticated analysis. Choose problems with multiple contributing factors and unclear solutions.

This solutions guide provides the framework for developing professional-level systematic problem-solving capabilities essential for process improvement consulting work.

---

## Navigation
**Project Assignment**: [[L1_C3_project|Return to Project Assignment]]  
**Next Chapter**: [[L1_C4_reading|Chapter 4: TO-BE Process Design and KPI Framework]]  
**Level Index**: [[../../Level1_index|Level 1 Index]]