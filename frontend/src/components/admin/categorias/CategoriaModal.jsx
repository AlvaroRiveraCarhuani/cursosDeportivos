import React, { useState, useEffect } from 'react';
import { FaTimes, FaSave } from 'react-icons/fa';
import styles from '../../../routes/admin/AdminDashboard.module.css'; 

const CategoriaModal = ({ editingCategory, onClose, onSave }) => {
    const [categoriaData, setCategoriaData] = useState({
        nombre: ''
    });

    useEffect(() => {
        if (editingCategory) {
            setCategoriaData({
                nombre: editingCategory.nombre || ''
            });
        } else {
            setCategoriaData({
                nombre: ''
            });
        }
    }, [editingCategory]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCategoriaData(prevData => ({ ...prevData, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(categoriaData);
    };

    return (
        <div className={styles.modalOverlay}>
            <div className={styles.modal}>
                <button className={styles.closeModalButton} onClick={onClose}>
                    <FaTimes />
                </button>
                <h3>{editingCategory ? 'Editar Categoría' : 'Crear Nueva Categoría'}</h3>
                <form onSubmit={handleSubmit}>
                    <div className={styles.formGroup}>
                        <label htmlFor="nombre">Nombre de la Categoría:</label>
                        <input
                            type="text"
                            id="nombre"
                            name="nombre"
                            value={categoriaData.nombre}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className={styles.modalActions}>
                        <button type="submit" className={styles.saveButton}>
                            <FaSave /> Guardar
                        </button>
                        <button type="button" onClick={onClose} className={styles.cancelButton}>
                            <FaTimes /> Cancelar
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default CategoriaModal;
