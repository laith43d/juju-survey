from orator.migrations import Migration


class Choice(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('choices') as table:
            table.increments('id')
            table.string('text', 100)
            table.integer('selected').default(0)
            table.integer('question_id').unsigned()
            table.foreign('question_id').references('id').on('questions').on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('choices')
