# Task 3: Review Summary

# Implement a function that takes the first 30 characters of each review and appends "…" to create a summary. (Bonus) Ensure that the summary does not cut off in the middle of a word.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

# look at each review individually
# split each review into a list of words
# iterate through that list and add each word to my summary while also counting the length of each word until I get to at least thirty

def summary_maker(reviews):
    for review in reviews:
        summary = []
        words = review.split()
        for word in words:
            if len(' '.join(summary)) <= 30:
                summary.append(word)

        ans = ' '.join(summary) + '...'
        print(ans)
        print(len(ans))

summary_maker(python_reviews)

