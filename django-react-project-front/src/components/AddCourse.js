import React from 'react';
import {ErrorMessage, Field, Form, Formik} from "formik";
import axios from "axios";

function AddCourse(props) {
    const handleSubmitCourse = (values, { setSubmitting }) => {
        axios.post('/course/all/', values)
            .then((response => {
                alert('Course added')
                setSubmitting(false)
            }))
            .catch(error => {
                alert('An error occured')
                setSubmitting(false)
            })
    }

    return (
        <div>
            <h1>Add Course</h1>
            <Formik
                initialValues={{ course_name: '', author: '', duration: 1 }}
                onSubmit={handleSubmitCourse}
            >
                {({ isSubmitting }) => (
                    <Form>
                        <Field placeholder={"Course name"} type="text" name="course_name" />
                        <p>Course Name</p>
                        <ErrorMessage name="course_name" component="div" />

                        <Field placeholder={"Author"} type="text" name="author" />
                        <p>Author</p>
                        <ErrorMessage name="author" component="div" />

                        <Field placeholder={"Duration (hours)"} type="number" name="duration" />
                        <p>Duration (hours)</p>
                        <ErrorMessage name="duration" component="div" />

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

export default AddCourse;
