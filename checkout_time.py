import heapq

def checkout_time(customers, n):
    # If there are no customers, the time required is 0.
    if not customers:
        return 0
    
    # If the number of tills is greater than or equal to the number of customers,
    # the time required is simply the maximum time of any individual customer.
    if n >= len(customers):
        return max(customers)
    
    # Initialize the tills (a min-heap to keep track of the time of each till)
    tills = [0] * n
    heapq.heapify(tills)  # Create a min-heap
    
    # Process each customer
    for time in customers:
        # Pop the till that will be free the earliest
        earliest_free_till = heapq.heappop(tills)
        
        # Add the customer's checkout time to this till
        heapq.heappush(tills, earliest_free_till + time)
    
    # The time required will be the maximum time across all tills after all customers have checked out
    return max(tills)

# Example usage:
customers = [5, 3, 8, 6]
n = 2
print(checkout_time(customers, n)) 