# L2.C3 Project: Database Design for TechServ Solutions

## Navigation
**Course**: [[../../index|Course Home]] > [[../../Level2_index|Level 2]] > [[L2_C3_reading|Chapter 3]] > Project  
**Previous**: [[L2_C3_reading|Chapter 3 Reading]]  
**Next**: [[L2_C3_solutions|Solutions Guide]]

---

## Project Overview

**Objective**: Design and implement a complete database structure for TechServ Solutions that supports automated workflow processes, enabling efficient customer management, service delivery, and billing automation.

**Duration**: 6-8 hours  
**Deliverable**: Database design package with ERD, implementation scripts, sample data, and integration documentation

## Business Context: TechServ Solutions

### Company Profile

TechServ Solutions is a 12-employee IT services company serving 85+ small businesses across the Denver metropolitan area. Founded in 2019, they've grown from basic break/fix services to comprehensive managed IT solutions.

**Current Challenges**:
- Customer data scattered across Excel spreadsheets, QuickBooks, and email
- Support tickets tracked in a shared Gmail inbox with inconsistent follow-up
- Project management happens in multiple tools with no central visibility
- Time tracking done manually on paper timesheets, leading to billing delays
- Contract renewals missed due to lack of systematic tracking
- Financial reporting requires hours of manual data compilation

**Growth Trajectory**:
- 2019: 15 customers, $180K revenue
- 2022: 65 customers, $850K revenue  
- 2024: 85 customers, $1.2M revenue (projected)
- Goal: 150 customers, $2.5M revenue by 2026

### Service Portfolio

**1. Break/Fix Support**
- **Description**: On-demand technical support for urgent issues
- **Pricing**: $125/hour, 4-hour minimum
- **Volume**: 45-60 tickets monthly
- **Typical Response**: 2-4 hours for initial contact

**2. Managed Services**
- **Description**: Monthly retainer with included support hours and proactive monitoring
- **Pricing Tiers**:
  - Essential: $500/month (8 hours included, $75/hour additional)
  - Professional: $1,200/month (20 hours included, $60/hour additional)
  - Enterprise: $2,500/month (50 hours included, $50/hour additional)
- **Volume**: 35 active contracts
- **Typical Terms**: 12-24 month agreements with annual price increases

**3. Project Implementation**
- **Description**: Fixed-scope technology implementations and upgrades
- **Pricing Range**: $2,000 (simple migrations) to $50,000 (complete infrastructure overhauls)
- **Volume**: 8-12 projects annually
- **Typical Duration**: 2-16 weeks depending on complexity

**4. Training Services**
- **Description**: End-user training on business applications and security practices
- **Pricing**: 
  - Group training: $150/hour (minimum 4 hours)
  - Individual training: $300/hour
  - Custom curriculum development: $200/hour
- **Volume**: 20-25 training sessions annually

### Automation Requirements

**Customer Onboarding Automation**:
- New customer signup triggers service tier assignment
- Contract setup workflow with automated document generation
- Welcome sequence with onboarding checklist items
- Integration with accounting system for billing setup

**Support Ticket Lifecycle**:
- Email-to-ticket conversion with automatic customer matching
- Priority assignment based on service tier and issue type
- Technician assignment using skills matching and availability
- SLA monitoring with escalation triggers
- Customer notification automation for status updates

**Project Management Workflows**:
- Project approval triggers resource allocation
- Milestone completion sends client notifications
- Budget tracking with overage alerts
- Delivery confirmation initiates invoice generation

**Billing Automation**:
- Time entry approval triggers invoice line item creation
- Monthly contract billing with hour consumption tracking
- Payment processing updates customer account status
- Overdue invoice follow-up sequence automation

**Contract Management**:
- Renewal notifications 90, 60, and 30 days before expiration
- Price increase notifications with approval workflows
- Service tier change impact calculations
- Contract compliance monitoring

## Database Design Requirements

### Core Entity Specifications

#### 1. Customers Entity
**Primary Information**:
- Company details (name, industry, size, tax ID)
- Primary contact information
- Service tier classification
- Account status and health scoring
- Geographic location for service routing

**Business Rules**:
- Each customer must have at least one contact person
- Service tier affects pricing and SLA terms
- Account status controls service availability
- Geographic location determines technician assignment

#### 2. Contacts Entity
**Primary Information**:
- Personal details (name, title, department)
- Communication preferences (email, phone, SMS)
- Role-based permissions (ticket creation, approval authority)
- Activity tracking (last login, communication history)

**Business Rules**:
- Multiple contacts per customer company
- One primary contact designated for billing/contracts
- Role permissions control access to different service types
- Communication preferences affect notification routing

#### 3. Service Contracts Entity
**Primary Information**:
- Contract terms (start date, duration, renewal options)
- Service tier and included hours
- Pricing structure (monthly fees, hourly rates)
- SLA commitments (response times, resolution targets)
- Contract status and modification history

**Business Rules**:
- Active contracts enable service delivery
- Hour banks track included vs. consumed hours
- Price changes require approval workflow
- Contract renewal creates new contract record

#### 4. Support Tickets Entity
**Primary Information**:
- Issue description and category classification
- Priority level and SLA requirements
- Status progression (open → assigned → in-progress → resolved → closed)
- Assignment details (technician, estimated hours)
- Resolution information and customer satisfaction

**Business Rules**:
- Tickets must link to valid customer contract
- Priority determines response time requirements
- Status changes trigger notification workflows
- Closed tickets become read-only

#### 5. Projects Entity
**Primary Information**:
- Project scope and deliverable specifications
- Budget allocation and resource assignments
- Phase/milestone breakdown with dependencies
- Timeline with start/end dates and critical path
- Approval status and change order tracking

**Business Rules**:
- Projects require approved statement of work
- Budget changes need customer approval
- Milestone completion gates next phase work
- Resource allocation affects capacity planning

#### 6. Time Entries Entity
**Primary Information**:
- Work performed details (description, category)
- Time allocation (start/end times, billable hours)
- Assignment linkage (ticket, project, or general work)
- Approval status and billing classification
- Rate information and invoice assignment

**Business Rules**:
- Time must link to customer work (ticket/project)
- Billable hours consume contract hour banks
- Approval required before invoice generation
- Rate determination based on work type and contract

#### 7. Employees Entity
**Primary Information**:
- Personal and employment details
- Skill certifications and specializations
- Billing rates by work category
- Availability and capacity planning
- Performance metrics and customer ratings

**Business Rules**:
- Active employees can be assigned work
- Skills determine assignment eligibility
- Rates vary by work type and customer tier
- Capacity limits prevent over-allocation

#### 8. Invoices Entity
**Primary Information**:
- Invoice details (number, date, terms)
- Line items from time entries and contracts
- Tax calculations and payment terms
- Status tracking (draft → sent → paid → overdue)
- Payment allocation and outstanding balances

**Business Rules**:
- Invoices generate from approved time entries
- Contract monthly fees auto-generate
- Payment terms vary by customer agreement
- Overdue invoices trigger collection workflows

### Relationship Specifications

**Customer-Contract Relationship** (1:M):
- One customer can have multiple active contracts
- Contracts have different service tiers and terms
- Historical contracts maintained for reporting

**Contract-Ticket Relationship** (1:M):
- Tickets must associate with active contracts
- Contract tier determines SLA requirements
- Hour consumption tracked against contract banks

**Employee-Assignment Relationship** (M:M):
- Employees can work on multiple tickets/projects
- Tickets/projects can have multiple assigned employees
- Assignment percentages for capacity planning

**Time Entry Junction Pattern**:
- Time entries link employees to work (tickets/projects)
- Support billing automation and reporting
- Enable detailed cost/profitability analysis

### Performance Requirements

**Query Performance Targets**:
- Customer lookup: < 100ms response time
- Ticket list views: < 500ms for 1000+ records
- Time entry reporting: < 2 seconds for monthly data
- Invoice generation: < 5 seconds for complex bills

**Concurrency Requirements**:
- 20+ simultaneous user sessions
- Real-time ticket updates across multiple users
- Concurrent time entry without conflicts
- Automated processes running during business hours

**Data Volume Planning**:
- 500+ customers within 3 years
- 5,000+ tickets annually
- 15,000+ time entries annually
- 7+ years historical data retention

## Project Deliverables

### 1. Entity-Relationship Diagram (25% of grade)

**Requirements**:
- Complete ERD showing all entities and relationships
- Proper notation for cardinality and relationship types
- Clear indication of primary keys, foreign keys, and important attributes
- Visual organization that demonstrates understanding of data relationships

**Tools Recommended**:
- Lucidchart, Draw.io, or similar diagramming tool
- Export as high-resolution PNG or PDF
- Include legend explaining notation used

**Evaluation Criteria**:
- Accuracy of relationships and cardinalities
- Completeness of entity attributes
- Professional visual presentation
- Logical organization and clarity

### 2. Database Schema Implementation (30% of grade)

**Requirements**:
- Complete SQL CREATE statements for all tables
- Appropriate data types for all fields
- Primary key and foreign key constraints
- Check constraints enforcing business rules
- Indexes optimized for automation query patterns

**File Format**:
- Single SQL file that creates complete schema
- Include comments explaining design decisions
- Test script that verifies constraint enforcement
- Index creation with performance justification

**Example Structure**:
```sql
-- TechServ Solutions Database Schema
-- Created for Level 2.3 Project

-- Create database and basic setup
CREATE DATABASE techserv_solutions;
USE techserv_solutions;

-- Create custom data types
CREATE TYPE service_tier AS ENUM ('essential', 'professional', 'enterprise');
CREATE TYPE ticket_status AS ENUM ('open', 'assigned', 'in_progress', 'resolved', 'closed');

-- Tables with full constraints and indexes
CREATE TABLE customers (
    -- Table definition with comments
);

-- Performance indexes
CREATE INDEX idx_performance_example ON table_name(column_list);
```

### 3. Sample Data and Queries (25% of grade)

**Sample Data Requirements**:
- Minimum 10 realistic records per major table
- Data relationships properly maintained
- Business scenarios covered (different service tiers, ticket types, project phases)
- Data quality demonstrates understanding of business domain

**Query Examples Required**:
```sql
-- 1. Customer service tier summary
-- 2. Monthly recurring revenue calculation
-- 3. Technician utilization reporting
-- 4. Overdue invoice identification
-- 5. Contract renewal pipeline
-- 6. Ticket SLA compliance
-- 7. Project profitability analysis
-- 8. Employee performance metrics
```

**Performance Analysis**:
- EXPLAIN plans for complex queries
- Index usage verification
- Optimization recommendations

### 4. Integration Documentation (20% of grade)

**API Endpoint Specifications**:
Document REST API endpoints for automation integration:
- Customer CRUD operations
- Ticket lifecycle management
- Time entry creation and approval
- Invoice generation triggers

**Data Validation Rules**:
- Input validation for automated data entry
- Business rule enforcement
- Error handling for constraint violations
- Data quality monitoring procedures

**Automation Integration Points**:
- Webhook endpoints for external system integration
- Batch processing procedures for bulk operations
- Real-time notification trigger conditions
- Reporting data export procedures

**Security Considerations**:
- Role-based access control implementation
- API authentication and authorization
- Data encryption for sensitive information
- Audit trail requirements

## Submission Requirements

### File Structure
```
[LastName]_TechServ_Database/
├── README.md (project overview and setup instructions)
├── documentation/
│   ├── ERD_diagram.png (entity relationship diagram)
│   ├── business_requirements.md (detailed requirements analysis)
│   └── integration_guide.md (API and automation documentation)
├── database/
│   ├── schema.sql (complete database creation script)
│   ├── sample_data.sql (realistic test data)
│   ├── queries.sql (example queries with explanations)
│   └── indexes.sql (performance optimization indexes)
└── testing/
    ├── test_data_validation.sql (constraint testing)
    ├── performance_tests.sql (query performance verification)
    └── integration_tests.sql (automation scenario testing)
```

### Quality Standards

**Professional Documentation**:
- Clear, concise writing suitable for technical stakeholders
- Proper SQL formatting and commenting
- Logical organization of all deliverable components
- Error-free code that executes successfully

**Business Alignment**:
- Database design supports all stated business requirements
- Automation integration points clearly identified
- Performance characteristics meet stated requirements
- Scalability considerations for projected growth

**Technical Excellence**:
- Proper normalization without over-engineering
- Appropriate use of constraints and indexes
- Efficient query design for common operations
- Security and data integrity protections

## Evaluation Criteria

### Database Design Quality (40%)
- **Excellent (36-40 points)**: Complete ERD with accurate relationships, proper normalization, all business requirements supported
- **Good (28-35 points)**: Minor issues with relationships or missing some business requirements
- **Needs Improvement (0-27 points)**: Major design flaws, incomplete relationships, or poor normalization

### Implementation Quality (30%)
- **Excellent (27-30 points)**: Clean SQL code, proper constraints, good performance optimization
- **Good (21-26 points)**: Minor syntax issues or missing some constraints
- **Needs Improvement (0-20 points)**: Significant coding errors or incomplete implementation

### Business Understanding (20%)
- **Excellent (18-20 points)**: Deep understanding of business requirements, realistic scenarios, practical automation integration
- **Good (14-17 points)**: Good business understanding with minor gaps
- **Needs Improvement (0-13 points)**: Poor understanding of business context or requirements

### Documentation Quality (10%)
- **Excellent (9-10 points)**: Professional, comprehensive documentation suitable for stakeholder review
- **Good (7-8 points)**: Good documentation with minor presentation issues
- **Needs Improvement (0-6 points)**: Poor documentation or incomplete deliverables

### Bonus Opportunities (+5 points each, max +10)
- **Advanced Features**: Implement stored procedures, triggers, or views that add business value
- **Performance Innovation**: Creative indexing or query optimization beyond requirements
- **Integration Excellence**: Detailed webhook/API specifications with working examples

---

## Chapter Links
- 📚 **Reading**: [[L2_C3_reading|Chapter 3 Reading]]
- 🧠 **Quiz**: [[L2_C3_quiz.html|Take the Databases & Entities Quiz]]
- ✅ **Solutions**: [[L2_C3_solutions|Solutions Guide]]

## Navigation
**Previous**: [[L2_C3_reading|Chapter 3 Reading]]  
**Next**: [[L2_C3_solutions|Solutions Guide]]  
**Up**: [[../../Level2_index|Level 2 Index]]