import petl as etl

class CSVCacheManager:
    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.create_cache_if_not_exists()

    def create_cache_if_not_exists(self):
        if not etl.exists(self.cache_file):
            # Create an empty cache file with headers
            etl.fromdicts([]).tocsv(self.cache_file)

    def add_record(self, record):
        # Add a new record to the cache
        table = etl.fromcsv(self.cache_file)
        table = etl.append(table, [record])
        table.tocsv(self.cache_file)

    def get_all_records(self):
        # Retrieve all records from the cache
        return etl.fromcsv(self.cache_file)

    def clear_cache(self):
        # Clear the cache by creating an empty file again
        self.create_cache_if_not_exists()

    def find_record(self, **criteria):
        # Find a record by given criteria
        table = etl.fromcsv(self.cache_file)
        return etl.select(table, **criteria)