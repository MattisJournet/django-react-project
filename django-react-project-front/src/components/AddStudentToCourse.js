import React from 'react';
import {ErrorMessage, Field, Form, Formik} from "formik";
import axios from "axios";

function AddStudentToCourse(props) {
    const handleSubmit = (values, { setSubmitting }) => {
        axios.post('/course/add-student-to-course/', values)
            .then((response => {
                alert('Student added')
                setSubmitting(false)
            }))
            .catch(error => {
                alert(error.response.data.detail)
                setSubmitting(false)
            })
    }

    return (
        <div>
            <h1>Add student to a course</h1>
            <Formik
                initialValues={{ student_id: '', course_id: '' }}
                onSubmit={handleSubmit}
            >
                {({ isSubmitting }) => (
                    <Form>
                        <Field placeholder={"Student ID"} type="number" name="student_id" />
                        <p>Student ID</p>
                        <ErrorMessage name="student_id" component="div" />

                        <Field placeholder={"Course ID"} type="number" name="course_id" />
                        <p>Course ID</p>
                        <ErrorMessage name="course_id" component="div" />

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

export default AddStudentToCourse;
