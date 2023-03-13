import React from 'react';
import axios from "axios";
import {ErrorMessage, Field, Form, Formik} from "formik";

function AddStudent(props) {
    const handleSubmitStudent = (values, { setSubmitting }) => {
        axios.post('/student/all/', values)
            .then((response => {
                alert('Student added')
                setSubmitting(false)
            }))
            .catch(error => {
                alert('An error occured')
                setSubmitting(false)
            })
    }

    return (
        <div>
            <h1>Add Student</h1>
            <Formik
                initialValues={{ last_name: '', first_name: '' }}
                onSubmit={handleSubmitStudent}
            >
                {({ isSubmitting }) => (
                    <Form>
                        <Field placeholder={"Last name"} type="text" name="last_name" />
                        <p>Last Name</p>
                        <ErrorMessage name="last_name" component="div" />

                        <Field placeholder={"First name"} type="text" name="first_name" />
                        <p>First Name</p>
                        <ErrorMessage name="first_name" component="div" />
                        <br/>
                        <button type="submit" disabled={isSubmitting}>
                            Submit
                        </button>
                    </Form>
                )}
            </Formik>
        </div>
    );
}

export default AddStudent;
