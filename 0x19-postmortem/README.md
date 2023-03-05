# 0x19. Postmortem

On March 1, 2023, from 10:00 AM to 11:00 AM PST, our web application experienced an outage, causing a complete loss of service for all users. The outage impacted the core functionality of our application, preventing users from accessing their accounts and using our service. Approximately 100% of users were affected.

## Timeline:

- 10:00 AM PST: The issue was detected by our monitoring system, which reported a sudden spike in errors and an increase in latency.
- 10:05 AM PST: The engineering team was notified of the issue, and began investigating potential root causes. At first, the team suspected a database issue, and began to investigate the database logs and connections.
- 10:15 AM PST: The team identified an issue with the database configuration, and attempted to rollback to a previous version of the database configuration. This did not resolve the issue, and the team began to investigate further.
- 10:30 AM PST: The team escalated the issue to the infrastructure team, suspecting that there may be an issue with the load balancer or networking configuration.
- 10:45 AM PST: The infrastructure team confirmed that there was a configuration issue with the load balancer, causing a misconfiguration of network routes. The team was able to identify and fix the issue, and began to restore service.
- 11:00 AM PST: Service was fully restored, and users were able to access the application once again.

## Root Cause and Resolution:

The root cause of the outage was a misconfiguration of the load balancer, which caused network routes to become misconfigured. This resulted in the inability of the application to serve requests, causing a complete loss of service for all users. The issue was resolved by the infrastructure team, who identified and fixed the misconfiguration of the load balancer.

## Corrective and Preventative Measures:

To prevent similar outages from occurring in the future, the following measures will be taken:

- Conduct a thorough review of load balancer configuration to ensure that network routes are properly configured.
- Increase the frequency of monitoring and alerting for load balancer issues.
- Develop a plan for rapid response and escalation in the event of a similar outage.
- Increase redundancy of the load balancer to prevent single points of failure.
- Conduct regular audits of infrastructure configurations to identify potential misconfigurations before they cause issues.

## Tasks to address the issue:

- Conduct a full audit of all load balancer configurations to ensure that network routes are properly configured.
- Increase monitoring and alerting for load balancer issues, and develop clear response and escalation plans.
- Implement redundancy for the load balancer to prevent single points of failure.
- Conduct regular audits of infrastructure configurations to identify potential issues before they cause outages.
