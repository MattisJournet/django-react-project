import React, {useEffect, useState} from 'react';
import axios from "axios";

function GetCourse(props) {
    const [course, setCourse] = useState()

    const getCourse = () => {
        axios.get('course/all/')
            .then(response => {
                setCourse(response.data)
            })
    }

    useEffect(() => {
        getCourse()
    }, [])

    if (!course) {
        return <p>Loading</p>
    }

    return (
        <table className="table m-5">
            <thead>
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Course name</th>
                <th scope="col">Author</th>
                <th scope="col">Students</th>
            </tr>
            </thead>
            <tbody>
            {course.map((value, index) => {
                return (
                    <tr key={index}>
                        <th scope="row">{value.id}</th>
                        <td>{value.course_name}</td>
                        <td>{value.author}</td>
                        <td>
                            {value.students.map((student, indexStudent) => {
                                return (
                                    <div key={indexStudent}>
                                        <span>{student.last_name} {student.first_name}, </span>

                                    </div>
                                )
                            })}
                        </td>
                    </tr>
                )
            })}

            </tbody>
        </table>
    );
}

export default GetCourse;
