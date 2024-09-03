import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(id, delay):
    print(f"Coroutine {id} starting to fetch data.")

    await asyncio.sleep(
        delay
    )  # Simulate a network request or I/O operation, using sleep()

    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    # After the TaskGroup code block, all tasks have completed (and the
    # previous block of code will stop blocking) and we can move on!

    results = [task.result() for task in tasks]  # Retrieve the results from the tasks

    for result in results:
        print(f"Received results: {result}")


# Run the main coroutine
asyncio.run(main())
