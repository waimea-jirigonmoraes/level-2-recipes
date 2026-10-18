#============================================================================
# Custom Flask CLI commands for project management
#
# Provides commands:
#  - flask db-reset   Delete and recreate database
#  - flask db-clear   Clear all data (with confirmation)
#  - flask db-show    Shows the DB schema and data
#  - flask db-schema  Shows the DB schema
#  - flask db-data    Shows the DB data
#============================================================================

import click
from app.helpers.log import get_console, get_logger

console = get_console()
logger  = get_logger()


