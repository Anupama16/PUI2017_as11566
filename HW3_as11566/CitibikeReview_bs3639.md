# Review of Citibike Assignment
**Assignment Author**: Anupama Santhosh

**Review Author**: Ben Steers

### Verify the null and alternative hypotheses
The idea looks good. The null hypothesis seems misleading as it is stated in terms of the weekend count over the weekday count which is the inverse measure of the amount that people are commuting. A better way to measure this would be the weekday count over the weekend count. This way a higher ratio equates to a higher level of commuting.

I would update the null hypothesis to be:
> The ratio of young people biking on *weekdays* over young people biking on *weekends* is *less than or equal* to the ratio of old people biking over *weekdays* to people biking on *weekends*.

The alternative hypothesis is missing, so that should be added as the inverse of the null hypothesis (i.e. instead of <= use >).

Also, the classification of old/young is not defined in the hypothesis. This should be clarified as some age threshold stated in the hypothesis.
E.g.
> The ratio of *people under 35* biking ... is *less than or equal* to the ratio of *people over 35* ...

### Verify that the data supports the project
The Citibike data provides the birth year so calculating and comparing the ages of users is not an issue. One caveat is that the age is only provided for Subscribers and is not listed for single use Customers. This means that the data being used for this is filled disproportionately with Subscribers and heavy Citibike users, and ignores all casual, unsubscribed riders. This is not necessarily an issue, as a percentage of Subscribers surely use Citibike on the weekends.

To be more explicit in the statement of the hypothesis, at the risk of becoming verbose, it could be stated as:
> The ratio of *Cikitbike Subscribers under 35* ...

### Choose an appropriate test
The test required needs to address whether there is a difference between two unpaired groups, as it can be assumed that the population of young and old Cikibike users are mutually distinct. The proper test for this is a Chi-squared test as it deals with comparing the differences of two categorical variables (young vs. old).

#### Comments/Suggestions
Overall it looks good! The suggestions given above should be considered to improve the clarity of the test. 
