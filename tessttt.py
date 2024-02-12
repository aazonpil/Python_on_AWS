arn = "arn:iam::123456789012:user/Development/product_1234/*"

# Find the start index by locating the second colon after "iam::" and add 1
start_index = arn.find("iam::") + 5

# Find the end index by locating the colon after the account ID
end_index = arn.find(":user", start_index)

# Extract the account ID using the identified indices
account_id = arn[start_index:end_index]

print(f"the aws_account_id is {account_id}")
