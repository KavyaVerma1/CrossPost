import { getToken } from 'next-auth/jwt';
import { createUploadthing, type FileRouter } from 'uploadthing/server';
import { NextRequest } from "next/server";

const f = createUploadthing();

export const ourFileRouter = {
  imageUploader: f({ image: { maxFileSize: '4MB' } })
    .middleware(async (req) => {
      const user = await getToken({ req: req as NextRequest });

      if (!user) throw new Error('Unauthorized');

      return { userId: user.id };
    })
    .onUploadComplete(async () => {}),
} satisfies FileRouter;

export type OurFileRouter = typeof ourFileRouter;
