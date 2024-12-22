def create_customer(db, customer_data):
    customers = db['customers']
    result = customers.insert_one(customer_data)
    print(f"Customer {customer_data['name']} added successfully!")

def read_customers(db):
    customers = db['customers']
    result = customers.find()
    print("\nУсі клієнти:")
    for customer in result:
        print(customer)

def update_customer(db, customer_id, updated_data):
    customers = db['customers']
    result = customers.update_one({"customer_id": customer_id}, {"$set": updated_data})
    if result.matched_count > 0:
        print(f"Customer with id {customer_id} updated successfully!")
    else:
        print(f"Customer with id {customer_id} not found.")

def delete_customer(db, customer_id):
    customers = db['customers']
    result = customers.delete_one({"customer_id": customer_id})
    if result.deleted_count > 0:
        print(f"Customer with id {customer_id} deleted successfully!")
    else:
        print(f"Customer with id {customer_id} not found.")
