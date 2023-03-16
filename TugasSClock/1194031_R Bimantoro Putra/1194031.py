import time

# Function to simulate a network delay
def network_delay():
    time.sleep(1)

# Cristian algorithm for synchronous clock
def sync_clock(server_time, rtt):
    now = time.time()
    network_delay()
    return now + (rtt / 2) + (server_time - now)

# Simulate server time from logistics server
gojek_server_time = time.time() - 60

# Simulate round-trip time between logistics server and shipping location
rtt = 2

# Synchronize the clock between the logistics server and shipping location
location_pemesan_time = sync_clock(gojek_server_time, rtt)

# Calculate the time difference between logistics server and shipping location
time_difference = location_pemesan_time - gojek_server_time

# Calculate the estimated time for a shipment to arrive at the shipping location
estimasi_sampai = time.time() + time_difference + 3600 # Add 1 hour for delivery time

# Print the results
print("Logistics server time:", time.ctime(gojek_server_time))
print("Round-trip time:", rtt)
print("Shipping location time:", time.ctime(location_pemesan_time))
print("Time difference:", time_difference, "seconds")
print("Estimated delivery time:", time.ctime(estimasi_sampai))
