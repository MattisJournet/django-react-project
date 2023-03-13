import React, {useEffect, useState} from 'react';
import axios from "axios";

const applyFilters = (author, query) => {
    return author.filter((author) => {
        let matches = true;

        if (query) {
            const properties = ['author'];
            let containsQuery = false;

            properties.forEach((property) => {
                if (author[property].toLowerCase().includes(query.toLowerCase())) {
                    containsQuery = true;
                }
            });

            if (!containsQuery) {
                matches = false;
            }
        }

        return matches;
    });
};

function GetCourse(props) {
    const [course, setCourse] = useState()
    const [query, setQuery] = useState('');

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
        return <p>Loading...</p>
    }

    const filteredCourse = applyFilters(course, query)

    return (
        <div>
            <div className={'d-flex justify-content-center mt-5'}>
                <input value={query} onChange={(e) => setQuery(e.target.value)} type="text" placeholder={"Search by author"}/>
            </div>
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
                {filteredCourse.map((value, index) => {
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
        </div>
    );
}

export default GetCourse;
