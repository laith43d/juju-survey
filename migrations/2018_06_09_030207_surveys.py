from orator.migrations import Migration


class Surveys(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('surveys') as table:
            table.increments('id')
            table.text('name')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('surveys')
