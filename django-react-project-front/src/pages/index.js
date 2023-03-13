import React from 'react';
import AddStudent from "../components/AddStudent";
import AddCourse from "../components/AddCourse";
import AddStudentToCourse from "../components/AddStudentToCourse";

const Index = () => {

    return (
        <div className={"d-flex justify-content-around mt-5"}>
            <AddStudent />
            <AddCourse />
            <AddStudentToCourse />
        </div>
    )

}

export default Index;
