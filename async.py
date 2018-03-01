from multiprocessing import Pool

def asynchronous_pool_order(func, args, object_list):
    pool = Pool()
    output_list = []
    multiple_results = [pool.apply_async(func, (*args, object_type))
                        for object_type in object_list]
    for result in multiple_results:
        value = result.get()
        output_list.append(value)
    return output_list
