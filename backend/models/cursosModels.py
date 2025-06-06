from data.conexion import obtenerConexion
import pymysql.cursors

class CursosModel:
    @staticmethod
    def crear_curso(data):
        conexion = obtenerConexion()
        if conexion is None:
            return {"error": "Error de conexión a BD"}

        try:
            with conexion.cursor() as cursor:
                sql_curso = """INSERT INTO cursos(nombre, descripcion, cupos, profesor_id, categoria_id)
                               VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(sql_curso, (
                    data['nombre'],
                    data['descripcion'],
                    data['cupos'],
                    data['profesor_id'],
                    data.get('categoria_id') 
                ))
                curso_id = cursor.lastrowid

                for horario in data['horarios']:
                    sql_horario = """INSERT INTO horarios(curso_id, dia, hora_inicio, hora_fin)
                                     VALUES (%s, %s, %s, %s)"""
                    cursor.execute(sql_horario, (
                        curso_id,
                        horario['dia'],
                        horario['hora_inicio'],
                        horario['hora_fin']
                    ))

                conexion.commit()
                return {
                    "id": curso_id,
                    "mensaje": "Curso creado exitosamente",
                    "nombre": data['nombre']
                }

        except pymysql.Error as e:
            conexion.rollback()
            return {"error": "Error en base de datos", "codigo": e.args[0], "mensaje": e.args[1]}
        except Exception as e:
            conexion.rollback()
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def obtener_cursos():
        conexion = obtenerConexion()
        if conexion is None:
            return {"error": "Error de conexión a BD"}

        try:
            with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT c.*,
                                u.name as profesor_nombre,
                                u.lastname as profesor_apellido,
                                cat.nombre as categoria_nombre
                         FROM cursos c
                         JOIN users u ON c.profesor_id = u.id
                         LEFT JOIN categorias cat ON c.categoria_id = cat.id"""
                cursor.execute(sql)
                cursos = cursor.fetchall()

                for curso in cursos:
                    cursor.execute(
                        "SELECT dia, hora_inicio, hora_fin FROM horarios WHERE curso_id = %s",
                        (curso['id'],)
                    )
                    horarios = cursor.fetchall()

                    horarios_serializables = []
                    for horario in horarios:
                        horarios_serializables.append({
                            'dia': horario['dia'],
                            'hora_inicio': str(horario['hora_inicio']),
                            'hora_fin': str(horario['hora_fin'])
                        })
                    curso['horarios'] = horarios_serializables
                return cursos

        except pymysql.Error as e:
            return {"error": "Error en base de datos", "codigo": e.args[0], "mensaje": e.args[1]}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def obtener_cursos_por_profesor(profesor_id):
        conexion = obtenerConexion()
        if conexion is None:
            return {"error": "Error de conexión a BD"}

        try:
            with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = """SELECT c.id, c.nombre, c.descripcion, c.cupos, c.profesor_id, c.categoria_id, cat.nombre as categoria_nombre
                         FROM cursos c
                         LEFT JOIN categorias cat ON c.categoria_id = cat.id
                         WHERE c.profesor_id = %s"""
                cursor.execute(sql, (profesor_id,))
                cursos = cursor.fetchall()

                for curso in cursos:
                    cursor.execute(
                        "SELECT dia, hora_inicio, hora_fin FROM horarios WHERE curso_id = %s",
                        (curso['id'],)
                    )
                    horarios = cursor.fetchall()
                    horarios_serializables = []
                    for horario in horarios:
                        horarios_serializables.append({
                            'dia': horario['dia'],
                            'hora_inicio': str(horario['hora_inicio']),
                            'hora_fin': str(horario['hora_fin'])
                        })
                    curso['horarios'] = horarios_serializables

                return cursos

        except pymysql.Error as e:
            return {"error": "Error en base de datos", "codigo": e.args[0], "mensaje": e.args[1]}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def actualizar_curso(curso_id, data):
        conexion = obtenerConexion()
        if conexion is None:
            return {"error": "Error de conexión a BD"}

        try:
            with conexion.cursor() as cursor:
                updates = []
                values = []

                if 'nombre' in data:
                    updates.append("nombre = %s")
                    values.append(data['nombre'])
                if 'descripcion' in data:
                    updates.append("descripcion = %s")
                    values.append(data['descripcion'])
                if 'cupos' in data:
                    updates.append("cupos = %s")
                    values.append(data['cupos'])
                if 'profesor_id' in data:
                    updates.append("profesor_id = %s")
                    values.append(data['profesor_id'])
                if 'categoria_id' in data: 
                    updates.append("categoria_id = %s")
                    values.append(data['categoria_id'])

                if updates:
                    sql_update_curso = f"UPDATE cursos SET {', '.join(updates)} WHERE id = %s"
                    values.append(curso_id)
                    cursor.execute(sql_update_curso, tuple(values))

                if 'horarios' in data:
                    sql_delete_horarios = "DELETE FROM horarios WHERE curso_id = %s"
                    cursor.execute(sql_delete_horarios, (curso_id,))

                    if data['horarios']:
                        sql_insert_horario = """
                            INSERT INTO horarios(curso_id, dia, hora_inicio, hora_fin)
                            VALUES (%s, %s, %s, %s)
                        """
                        for horario in data['horarios']:
                            cursor.execute(sql_insert_horario, (
                                curso_id,
                                horario['dia'],
                                horario['hora_inicio'],
                                horario['hora_fin']
                            ))

                conexion.commit()
                return {
                    "id": curso_id,
                    "mensaje": "Curso actualizado exitosamente"
                }

        except pymysql.Error as e:
            conexion.rollback()
            return {"error": "Error en base de datos", "codigo": e.args[0], "mensaje": e.args[1]}
        except Exception as e:
            conexion.rollback()
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def eliminar_curso(id):
        conexion = obtenerConexion()
        if conexion is None:
            return {"error": "Error de conexión a BD"}
        try:
            with conexion.cursor() as cursor:
                sql = "DELETE from cursos where id = %s"
                cursor.execute(sql, (id,))
                conexion.commit()
            return {"message": "Curso eliminado exitosamente"}
        except Exception as e:
            return {"error": "Error al eliminar curso",
            "detalles": str(e)}
        finally:
            conexion.close()
