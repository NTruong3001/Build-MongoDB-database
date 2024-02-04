function loadEducations() {
    const bulkInsert = db.educations.initializeUnorderedBulkOp();
    const documents = db.full.find({});

    documents.forEach(function (doc) {
        const element = {
            education: doc.education,
            education_num: doc.education_num
        };
        bulkInsert.find(element).upsert().replaceOne(element);
    });

    bulkInsert.execute();
    return true;
}

function loadOccupations() {
    const bulkInsert = db.occupations.initializeUnorderedBulkOp();
    const documents = db.full.find({});

    documents.forEach(function (doc) {
        const element = {
            occupation: doc.occupation,
            workclass: doc.workclass,
            hours_per_week: doc.hours_per_week
        };
        bulkInsert.find(element).upsert().replaceOne(element);
    });

    bulkInsert.execute();
    return true;
}

function loadRelationships() {
    const bulkInsert = db.relationships.initializeUnorderedBulkOp();
    const documents = db.full.find({});

    documents.forEach(function (doc) {
        const element = {
            marital_status: doc.marital_status,
            relationship: doc.relationship
        };
        bulkInsert.find(element).upsert().replaceOne(element);
    });

    bulkInsert.execute();
    return true;
}

function loadFinances() {
    const bulkInsert = db.finances.initializeUnorderedBulkOp();
    const documents = db.full.find({});

    documents.forEach(function (doc) {
        const element = {
            total: doc.total,
            capital_gain: doc.capital_gain,
            capital_loss: doc.capital_loss,
            income_bracket: doc.income_bracket
        };
        bulkInsert.find(element).upsert().replaceOne(element);
    });

    bulkInsert.execute();
    return true;
}

function loadUsers() {
    const bulkInsert = db.users.initializeUnorderedBulkOp();
    const documents = db.full.find({});

    documents.forEach(function (doc) {
        const userElement = {
            age: doc.age,
            gender: doc.gender,
            race: doc.race,
            native_country: doc.native_country
        };

        const education = db.educations.findOne({
            education: doc.education
        });
        userElement.education_id = education._id;

        const occupation = db.occupations.findOne({
            occupation: doc.occupation,
            workclass: doc.workclass,
            hours_per_week: doc.hours_per_week
        });
        userElement.occupation_id = occupation._id;

        const finance = db.finances.findOne({
            total: doc.total,
            capital_gain: doc.capital_gain,
            capital_loss: doc.capital_loss,
            income_bracket: doc.income_bracket
        });
        userElement.finance_id = finance._id;

        const relationship = db.relationships.findOne({
            marital_status: doc.marital_status,
            relationship: doc.relationship
        });
        userElement.relationship_id = relationship._id;

        bulkInsert.find(userElement).upsert().replaceOne(userElement);
    });

    bulkInsert.execute();
    return true;
}
