import sys

sys.path.append('/Users/nguyenthanhvinh/Documents/PYTHON/Project/BuddaMind/modules')


# Run once to create the table
from modules.database import Base, engine
from modules.models import User

Base.metadata.create_all(bind=engine)
print("✅ Tables created!")
