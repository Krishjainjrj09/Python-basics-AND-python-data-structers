# Step 1 — Create the base Connector class #

'''Define a base Connector class with one method, fetch(), that raises NotImplementedError.'''

class Connector:

    def fetch(self):
        raise NotImplementedError("Subclasses must implement fetch()")


# Step 2 — Create two subclasses #

'''Create two subclasses of Connector, each overriding fetch() differently.

I am creating:

APIConnector
DatabaseConnector'''

class APIConnector(Connector):

    def fetch(self):
        return "Fetching data from API"


class DatabaseConnector(Connector):

    def fetch(self):
        return "Fetching data from Database"

api = APIConnector()
database = DatabaseConnector()

print(api.fetch())
print(database.fetch())



# Step 3 — Create LoggingMixin #
class LoggingMixin:

    def log(self, message):
        print(f"LOG: {message}")

'''Now we want our API connector to have logging.'''

class LoggedAPIConnector(LoggingMixin, APIConnector):

    def fetch(self):
        self.log("API fetch started")
        return "Fetching data from API"

connector = LoggedAPIConnector()

print(connector.fetch())



# Step 4 — Create the diamond hierarchy #

class Connector:

    def __init__(self):
        print("Connector initialized")

    def fetch(self):
        raise NotImplementedError("Subclasses must implement fetch()")


class APIConnector(Connector):

    def fetch(self):
        return "Fetching data from API"


class DatabaseConnector(Connector):

    def fetch(self):
        return "Fetching data from Database"


class LoggingMixin(Connector):

    def __init__(self):
        print("LoggingMixin initialized")

    def log(self, message):
        print(f"LOG: {message}")

class LoggedAPIConnector(LoggingMixin, APIConnector):

    def fetch(self):
        self.log("API fetch started")
        return "Fetching data from API"


# Step 5 — Print the MRO #

print(LoggedAPIConnector.__mro__)


# Step 6 — Trigger the diamond problem #

class LoggingMixin(Connector):

    def __init__(self):
        Connector.__init__(self)
        print("LoggingMixin initialized")
class APIConnector(Connector):

    def __init__(self):
        Connector.__init__(self)
        print("APIConnector initialized")

class LoggedAPIConnector(LoggingMixin, APIConnector):

    def __init__(self):
        LoggingMixin.__init__(self)
        APIConnector.__init__(self)

connector = LoggedAPIConnector()


# Step 7 — Fix it using super() #

'''Connector.__init__(self)

super().__init__()'''


# Correct Connector #
class Connector:

    def __init__(self):
        print("Connector initialized")

    def fetch(self):
        raise NotImplementedError("Subclasses must implement fetch()")

    
# Coreect API connector #
class APIConnector(Connector):

    def __init__(self):
        super().__init__()
        print("APIConnector initialized")

    def fetch(self):
        return "Fetching data from API"

# Correct LoggingMixin #

class LoggingMixin(Connector):

    def __init__(self):
        super().__init__()
        print("LoggingMixin initialized")

    def log(self, message):
        print(f"LOG: {message}")

# Logged API connector #

class LoggedAPIConnector(LoggingMixin, APIConnector):

    def __init__(self):
        super().__init__()
        print("LoggedAPIConnector initialized")

    def fetch(self):
        self.log("API fetch started")
        return "Fetching data from API"

connector = LoggedAPIConnector()



class Connector:

    def __init__(self):
        print("Connector initialized")

    def fetch(self):
        raise NotImplementedError("Subclasses must implement fetch()")


class APIConnector(Connector):

    def __init__(self):
        super().__init__()
        print("APIConnector initialized")

    def fetch(self):
        return "Fetching data from API"


class DatabaseConnector(Connector):

    def __init__(self):
        super().__init__()
        print("DatabaseConnector initialized")

    def fetch(self):
        return "Fetching data from Database"


class LoggingMixin(Connector):

    def __init__(self):
        super().__init__()
        print("LoggingMixin initialized")

    def log(self, message):
        print(f"LOG: {message}")


class LoggedAPIConnector(LoggingMixin, APIConnector):

    def __init__(self):
        super().__init__()
        print("LoggedAPIConnector initialized")

    def fetch(self):
        self.log("API fetch started")
        return "Fetching data from API"


# Create objects
api = APIConnector()
database = DatabaseConnector()
logged_api = LoggedAPIConnector()

# Call fetch()
print(api.fetch())
print(database.fetch())
print(logged_api.fetch())

# Print Method Resolution Order
print("\nMRO of LoggedAPIConnector:")
print(LoggedAPIConnector.__mro__)