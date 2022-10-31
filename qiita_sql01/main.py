import sqlite3


class DB:
    DB_NAME = "student.db"

    def __init__(self, filename) -> None:
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()

        with open(filename, "r") as f:
            sql_file = f.read()

        cursor.executescript(sql_file)
        conn.close()

    def execute(self, sql: str) -> None:
        print("*****" * 5)
        print(f"{sql}")
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()

        for row in cursor.execute(sql):
            print(row)

        print()


def main():
    db = DB("./init.sql")

    sql = """
    SELECT name
    FROM students
    WHERE gender='男'
    """
    db.execute(sql)

    sql = """
    SELECT DISTINCT name
    FROM students
    INNER JOIN results ON students.id=results.student_id
    WHERE results.score <= 30
    """
    db.execute(sql)

    sql = """
    SELECT gender, MAX(SCORE)
    FROM students
    INNER JOIN results ON students.id=results.student_id
    GROUP BY students.gender
    ORDER BY results.score DESC
    """
    db.execute(sql)

    sql = """
    SELECT subject, AVG(score) AS avg_score
    FROM results
    GROUP BY results.subject
    HAVING AVG(score) <= 50
    """
    db.execute(sql)

    # sql = """
    # SELECT
    #     r1.*,
    #     (
    #         SELECT
    #             AVG(r2.score)
    #         FROM
    #             results r2
    #         WHERE
    #             r1.subject=r2.subject
    #
    #     ) AS subject_avg_score
    # FROM results r1
    # """
    # db.execute(sql)
    sql = """
    SELECT students.name
    FROM students
    WHERE id NOT IN (
        SELECT results.student_id
        FROM results
        WHERE results.subject='理科'
    )
    """

    db.execute(sql)


if __name__ == "__main__":
    main()
