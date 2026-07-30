'''
In this Question, we have two different scenarios:
I: you can choose not to allocate money to a/some company/companies
II: you must allocate at least 1 to every comapny

'''
n <- 10          
k <- 4         
result_1 <- choose(n + k - 1, k - 1)
print(paste("the first scenario:", result_1))


remaining <- n - k
result_2 <- choose(remaining + k - 1, k - 1)
print(paste("the second scenario:", result_2))
