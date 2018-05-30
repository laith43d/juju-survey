from orator.migrations import Migration


class Question(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('questions') as table:
            table.increments('id')
            table.string('text', length = 500)
            table.integer('survey_id').unsigned()
            table.foreign('survey_id').references('id').on('surveys').on_delete('cascade')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('questions')
