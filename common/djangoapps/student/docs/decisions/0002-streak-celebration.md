Streak Celebration
---------------------

Status
------
Accepted

Context
-------
Adding a celebration for when a learner visits the learning mfe for 3 days in a row.


Relevant Ticket:
https://openedx.atlassian.net/browse/AA-304

Decisions
--------

1. **Retrieving streak celebration data**
We use the course home and courseware metadata APIs to retrieve the data determining whether we should celebrate a streak.
Some MFEs implement progressive loading, where individual requests only retrieve the data necessary for a given component. However, the learning MFE has gone the direction of retrieving all the necessary data upfront.

2. **No custom caching for streak celebration data**
Although the streak celebration data cannot change more than once per day, it will be retrieved on every page load. This is because the streak celebration data comes through the course home and courseware metadata APIs. We considered adding custom caching for the streak celebration data, but decided against it in order to avoid overcomplicating the metadata APIs.

3. **Date cutoff in user's timezone**
Once a user visits the learning MFE, their streak will not increment until midnight in their timezone.
The decision was to use the user's timezone and not UTC, to make each day of the streak more closely correspond to separate days for the user.

4. **Continue tracking streak after celebration** 
edx-platform continues to record the streak celebration fields after a celebration has ocurred.
This means that it should be relatively straightforward to modify the code to add additional streaks in addition to the 3 day streak if we would like to in the future.
