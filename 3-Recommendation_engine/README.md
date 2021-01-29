## Types of Recommendations
1. **Knowledge Based Recommendations**
> Recommend the most popular items for all the users, used for Website trending, rare/luxury items, often applied with filters.
2. **Collaborative Filtering Based Recommendations**
> Collaborative filtering is a method of making recommendations based only on the interactions between users and items.there are two main branches: 
 - Model Based Collaborative Filtering
 - Neighborhood Based Collaborative Filtering (User-based, item-based)

3. **Content Based Recommendations**
> Content based recommendations are when we use information about the users or items to assist in our recommendations.
You will learn why sometimes one metric works better than another by looking at a specific situation where one metric provides more information than another.

### Business Cases For Recommendations
Four ideas needed for businesses to implement successful recommendations to drive revenue, which include:
- Relevance
- Novelty
- Serendipity
- Increased Diversity

### Similarity Metrics
In order to implement Neighborhood Based Collaborative Filtering, need some ways to measure the similarity between two users (or two items) including:
- **Pearson's correlation coefficient:** a measure related to the strength and direction of a linear relationship.
- **Spearman's correlation coefficient:** Spearman's correlation is what is known as a non-parametric statistic,which is calculated similarly to Pearson's correlation. However, instead of using the raw data, we use the rank of each value.
- **Kendall's Tau:** Similar to both of the previous measures, Kendall's Tau is always between -1 and 1, where -1 suggests a strong, negative relationship between two variables and 1 suggests a strong, positive relationship between two variables.
Kendall's Tau has smaller variability when using larger sample sizes. However Spearman's measure is more computationally efficient, as Kendall's Tau is O(n^2) and Spearman's correlation is O(nLog(n)).
- **Euclidean Distance**
- **Manhattan Distance**

