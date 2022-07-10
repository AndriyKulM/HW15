"""002_create_rel_between_tables

Revision ID: 002_create_rel_between_tables
Revises: 001_create_authors_books_tables
Create Date: 2022-07-08 20:52:56.362420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_rel_between_tables'
down_revision = '001_create_authors_books_tables'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("authors", sa.Column("book_id_", sa.Integer, sa.ForeignKey("books.book_id")))


def downgrade() -> None:
    op.drop_column("authors", "book_id_")
